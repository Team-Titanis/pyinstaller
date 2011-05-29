# -*- mode: python -*-

__testname__ = 'test_getfilesystemencoding'

a = Analysis([os.path.join('support/_mountzlib.py'),
              os.path.join('support/useUnicode.py'),
              __testname__ + '.py'],
             pathex=[])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build', 'pyi.' + config['target_platform'], __testname__ + '.exe'),
          debug=False,
          strip=False,
          upx=False,
          console=1 )
coll = COLLECT(exe,
               a.binaries,
               strip=False,
               upx=False,
               name=os.path.join('dist', __testname__),)