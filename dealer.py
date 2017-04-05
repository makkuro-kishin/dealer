#!/usr/bin/python3

try:
    import sys
    import modules.controller
except Exception as import_error:
    print('[FAIL] Unable to start controller!\n', import_error, '\nAborting...', sep='')
    raise SystemExit
else:
    print('Welcome to Dealer.')


modules.controller.main()