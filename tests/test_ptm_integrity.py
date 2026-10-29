"""Integrity checks for the PTM transcription. Does not modify any source file."""
import hashlib, json, pathlib, re
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
MD = DOCS / 'KA-200-B200-PTM.md'
MANIFEST = DOCS / 'KA-200-B200-PTM_manifesto.json'
PDF = DOCS / 'KA-200-B200-PTM.pdf'
EXPECTED_PDF_SHA = '6835a8102c8f600c3b39aa34d2b53f9a848790321447136ec2cd821af245986d'

PROTECTED = {
    'docs/KA-200-B200-PTM.pdf': EXPECTED_PDF_SHA,
    'docs/KA-200-B200-POH.pdf': '373b77fd2baf52d3becd6d02efa6fa3cb447e77c0c9329057a94307c8e3cbbdb',
    'docs/KA-200-B200-POH_completo.md': 'b42d53f3eb3b3cdae66648fbd6a35aef2159951b347c800745aecb8a2a4374bc',
    'docs/KA-200-B200-POH_corrigido.md': '6dec31a605129942ebe6ae1bcbd4d8ea65f32dbd1c59f12b96973a4a706231d4',
    'docs/KA-200-B200-POH_controle.md': '728cdea9e7fb728e8c1fcb9f6fefab8cc71cd28b10a9133da8172e21ee830fb4',
    'docs/KA-200-B200-POH_prompt_continuacao.md': 'c7b663779e01c833ceb94c3e85749df9098b0635a0619ac9b6eafe4169b34f36',
    'docs/KA-200-B200-PTM_completo.md': '9b466886a6d578f5be038c83c01f799064bedf52e328f1eb2edb925c07bdd48b',
    'docs/KA-200-B200-PTM_corrigido.md': '1593cf2170a26ec27db09ca86f61fe521e3e3411f396b2b74d00e88e7701d39a',
    'docs/KA-200-B200-PTM_docling/manifesto.json': 'cb7087fb259856b489cdbc1b0b2307409e41cd166a59b616f262192112ff4f92',
}

@pytest.fixture(scope='module')
def text():
    return MD.read_text(encoding='utf8')

@pytest.fixture(scope='module')
def manifest():
    return json.loads(MANIFEST.read_text(encoding='utf8'))

def chunk(text, n):
    m = re.search(rf'<!-- PTM:PAGE:{n:03d} START -->\n<!-- PTM:STATUS:[a-z]+ -->\n(.*?)<!-- PTM:PAGE:{n:03d} END -->', text, re.S)
    assert m, f'missing chunk {n}'
    return m.group(1)

def test_source_pdf_hash_and_pages():
    assert hashlib.sha256(PDF.read_bytes()).hexdigest() == EXPECTED_PDF_SHA
    pymupdf = pytest.importorskip('pymupdf')
    with pymupdf.open(PDF) as d:
        assert len(d) == 382

def test_markers_sequential_and_status(text, manifest):
    starts = [int(x) for x in re.findall(r'<!-- PTM:PAGE:(\d+) START -->', text)]
    ends = [int(x) for x in re.findall(r'<!-- PTM:PAGE:(\d+) END -->', text)]
    assert starts == list(range(1, 383))
    assert ends == list(range(1, 383))
    assert manifest['physical_pages'] == 382
    assert manifest['reviewed_through'] == 200
    for e in manifest['pages']:
        n = e['physical']
        expected = 'revisada' if n <= 200 else 'pendente'
        assert e['status'] == expected
        assert f'<!-- PTM:PAGE:{n:03d} START -->\n<!-- PTM:STATUS:{expected} -->' in text

def test_reviewed_chunk_hashes(text, manifest):
    for e in manifest['pages']:
        if e['status'] != 'revisada':
            assert e['sha256'] is None
            continue
        h = hashlib.sha256(chunk(text, e['physical']).encode('utf8')).hexdigest()
        assert h == e['sha256'], f"hash mismatch page {e['physical']}"

def test_pending_chunks_have_no_automatic_conversion(text):
    for n in range(201, 383):
        c = chunk(text, n)
        assert 'Pendente de revisão' in c
        assert 'KA-200-B200-PTM_imagens' not in c
        assert 'assets/ptm/' not in c

def test_reviewed_chunks_have_facsimile_and_no_old_converter(text):
    for n in range(1, 201):
        c = chunk(text, n)
        assert f'assets/ptm/page-{n:03d}.png' in c
        assert 'KA-200-B200-PTM_imagens' not in c

def test_local_links_and_images_exist(text):
    for target in re.findall(r'!?\[[^\]]*\]\(([^)\s]+)\)', text):
        if target.startswith(('http://', 'https://', 'mailto:')):
            continue
        pathpart = target.split('#', 1)[0]
        if not pathpart:
            continue
        p = (DOCS / pathpart).resolve()
        assert p.exists(), f'broken link {target}'
        if target.lower().endswith('.png'):
            assert p.stat().st_size > 0
            assert p.read_bytes()[:8] == b'\x89PNG\r\n\x1a\n'
        if pathpart.endswith('.pdf') and '#page=' in target:
            page = int(target.split('#page=')[1])
            assert 1 <= page <= 382

def test_markdown_tables_rectangular(text):
    for n in range(1, 201):
        lines = chunk(text, n).splitlines()
        i = 0
        while i < len(lines):
            if lines[i].lstrip().startswith('|'):
                block = []
                while i < len(lines) and lines[i].lstrip().startswith('|'):
                    block.append(lines[i]); i += 1
                assert len(block) >= 2, f'table too short page {n}'
                assert re.match(r'^\|(\s*:?-{3,}:?\s*\|)+\s*$', block[1]), f'bad separator page {n}: {block[1]}'
                counts = [len(re.split(r'(?<!\\)\|', ln)) for ln in block]
                assert len(set(counts)) == 1, f'ragged table page {n}: {counts}'
            else:
                i += 1

@pytest.mark.parametrize('path,expected', sorted(PROTECTED.items()))
def test_protected_files_unchanged(path, expected):
    assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected

def test_source_anomalies_preserved(text):
    c12 = chunk(text, 12)
    for word in ('baltery', 'interconnecled', 'buttery', 'SO-amp'):
        assert word in c12
    c37 = chunk(text, 37)
    assert 'ELECTRICAL POWER SYSTEMS' in c37 and 'ELECTRICAL POWER SYSTEMES' not in c37
    c58 = chunk(text, 58)
    assert sum(1 for ln in c58.splitlines() if ln.startswith('| 70 to 75%')) == 1  # second group intentionally lacks this row
    c84 = chunk(text, 84)
    assert '| **DOOR UNLOCKED** | Cabin altitude exceeds 12,500 feet' in c84
    assert '| **ALT WARN** | Fire in right engine compartment' in c84

def test_questions_choices_separated(text):
    c64 = chunk(text, 64)
    assert 'A. 28-volt, 24 ampere-hour  \nB. 24-volt, 34/36 ampere-hour' in c64

def test_control_inventory_matches_manifest(manifest):
    control = (DOCS / 'KA-200-B200-PTM_controle.md').read_text(encoding='utf8')
    rows = re.findall(r'^\| \[(\d+)\]\(KA-200-B200-PTM\.pdf#page=\d+\) \|', control, re.M)
    assert [int(x) for x in rows] == list(range(1, 383))
    for e in manifest['pages']:
        if e['status'] == 'revisada':
            assert e['sha256'] in control


def test_batch2_source_anomalies_preserved(text):
    assert 'aDownstream' in chunk(text, 128)
    assert 'extends form 85 to 100 psi' in chunk(text, 153)
    assert 'D. Indication speeds' in chunk(text, 200)
    assert 'PRIOR TO BB-1439, 1444 AND SUBSEQUENT' in chunk(text, 150)
    assert '12. These values are time limited to five minutes.' in chunk(text, 151)
    assert 'MEL-T-5624' in chunk(text, 108)
    assert 'B-1192' in chunk(text, 133)

def test_batch2_critical_tables_present(text):
    c150 = chunk(text, 150)
    assert c150.count('| OPERATING CONDITION | SHP |') == 2
    assert '| LOW IDLE | --- | --- | 750 (6) | 22,875 | 61 (min) |' in c150.replace('<br>', '')
    c151 = chunk(text, 151)
    assert '| LOW IDLE | --- | --- | 660 (6) | 19,500 | 52 (min) |' in c151.replace('<br>', '')
    c153 = chunk(text, 153)
    assert c153.count('| INSTRUMENT | RED LINE MINIMUM LIMIT |') == 3
    assert '| OIL PRESSURE \\*\\* | 60 psi | --- | 100 psi to 135 psi | 200 psi |' in c153
    c163 = chunk(text, 163)
    assert '| PSI MINIMUM | 190 | 220 | 250 | 290 | 340 | 390 | 455 | 525 | 605 |' in c163
    assert '| PSI MAXIMUM | 240 | 275 | 315 | 365 | 420 | 480 | 550 | 635 | 730 |' in c163

def test_batch2_reviewed_ranges(manifest):
    assert manifest.get('reviewed_ranges') == [[1, 100], [101, 200]]
    assert sum(1 for e in manifest['pages'] if e['status'] == 'revisada') == 200
