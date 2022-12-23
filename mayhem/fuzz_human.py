#!/usr/bin/python3
import atheris
import sys


with atheris.instrument_imports():
    import humanize

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    humanize.intcomma(fdp.ConsumeInt(128))
    humanize.intword(fdp.ConsumeInt(128))
    humanize.apnumber(fdp.ConsumeInt(128))
    humanize.naturalsize(fdp.ConsumeInt(128), fdp.ConsumeBool(), fdp.ConsumeBool())
    humanize.fractional(fdp.ConsumeRegularFloat())
    humanize.scientific(fdp.ConsumeRegularFloat())



def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
