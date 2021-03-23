import os
import lzma

def concat(files, arcname = "archive.sfc"):
    with open(arcname, "wb") as f:
        f.write(b"SSFC")
    for file in files:
        data = open(file, "rb").read()
        with open(arcname, "ab") as f:
            f.write(bytes(file.split("/")[-1], "ascii"))
            f.write(b"filenameSeparator")
            f.write(data)
            f.write(b"fileDataEnd")

def deconcat(arcname = "archive.sfc"):
    with open(arcname, "rb") as f:
        data = f.read()[4:][:-3]
        fdatas = data.split(b"fileDataEnd")
        for fdata in fdatas:
            fn = fdata.split(b"filenameSeparator")[0]
            el = fdata.split(b"filenameSeparator")[1]
            with open(fn, "wb") as f:
                f.write(el)