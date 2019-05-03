# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/shreya/APCSP/latest/APCSP-create/src/main/python/main.py'],
             pathex=['/Users/shreya/APCSP/latest/APCSP-create/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/shreya/Documents/venv/lib/python3.7/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/var/folders/gh/_djj3s1d7pgbfylflkw3j46r0000gn/T/tmptep3kr3f/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='PrefixCalc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/shreya/APCSP/latest/APCSP-create/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='PrefixCalc')
app = BUNDLE(coll,
             name='PrefixCalc.app',
             icon='/Users/shreya/APCSP/latest/APCSP-create/target/Icon.icns',
             bundle_identifier=None)
