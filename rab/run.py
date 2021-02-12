import sys
try:
    import sourcedefender
except Exception as e:
    print('Please check you have install requirements.txt successfully.\nRefer to step 10 in Github: {}'.format(e))
    sys.exit(0)
try:
    import rab
except Exception as e:
    print("Encounter unexpected error: {}".format(e))