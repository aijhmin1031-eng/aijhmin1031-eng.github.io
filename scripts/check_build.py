#!/usr/bin/env python3
"""배포 전 필수 검증 — YAML 문법 + front matter. 통과 못하면 푸시하지 말 것.
사용: python3 scripts/check_build.py   (repo 루트에서)
"""
import glob, sys, io
try:
    import yaml
except ImportError:
    sys.exit('pyyaml 필요: pip install pyyaml')

fail = []

# 1) _data/*.yml 문법
for f in glob.glob('_data/*.yml'):
    try:
        yaml.safe_load(io.open(f, encoding='utf-8'))
    except Exception as e:
        fail.append(f'{f}: {str(e).splitlines()[0]}')

# 2) _config.yml 문법
try:
    yaml.safe_load(io.open('_config.yml', encoding='utf-8'))
except Exception as e:
    fail.append(f'_config.yml: {str(e).splitlines()[0]}')

# 3) 글·페이지 front matter 문법
for f in glob.glob('_posts/*.md') + glob.glob('*.md'):
    if f in ('README.md', 'CLAUDE.md'):
        continue
    s = io.open(f, encoding='utf-8').read()
    if not s.startswith('---'):
        continue
    fm = s.split('---', 2)
    if len(fm) < 3:
        fail.append(f'{f}: front matter 닫히지 않음')
        continue
    try:
        yaml.safe_load(fm[1])
    except Exception as e:
        fail.append(f'{f}: front matter — {str(e).splitlines()[0]}')

if fail:
    print('❌ 검증 실패 — 푸시하지 말 것')
    for x in fail:
        print('  -', x)
    sys.exit(1)
print('✅ 검증 통과 — 배포 가능')
