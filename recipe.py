import time

from helpers import cbc_dec, valid_pad

key = b"\x81\xf8\xb5\xf0\xf0\xf0\xaan\x07\xbd\x81\xc59\xbc3UGV\x96J\xf3-~\xff0G\x842\x06\xed\xad\xa8"
iv = b"uf\xd1\x7f\xce\xf2'5\xfe\xf2\xd5tNs\xa2L"
ciphertext_v1 = b'\xf5\x95\t\xa1\x13\xbf\x82T\xc9\xf1x\xec\x9dO\x1a\xed1w\xfbH\xf7\xd4}\xd5\xa3\xf5\xf8\xd5<\xefy\xe7[&\x02j\x82\xd4Y\xffZdi\x82,\x04\x14Z\xc9\xa9\x82\xd3\x9c\xad{\xb4\xbe\xf0\xfdS\xa4K{d'
ciphertext_v2 = b'\xa2i\xbe\r=\xe8\xa0\x9d$\x1f\x9d\xfe\xe0\x03\xfb("\xb8\x1c\x89\x02\xbc\xf7\x89/\x03q^+\x86swF\x99\x9aLP\x82%o\xee\xf5>\x9a)+Et\xa0\x7f\x11\x94\x7f\x1a\x07\xbd\xe3\xe8q\xb7\xc2\xfa(q\xa2\xfbF8\xfc2-\x1b\xb6g\x8f\x8d\x16\xf0\x1clj0.\x0b{*I\xbep\x04J`lK\rr\n\r\x97\x83V\xa3\x0c=P\xd0\xe4fA\xdf\x99\x85+\xbby\xd4\x99\x00\xab\x85\x9c\xd8\xda\x7f\x12\xeeo-\x12W\x93\x8ft#X"\xff\x1d\x81\xc3v^ui\x1eJ\x1au\x0cV\xfd\x95\xd7\x03\x80z\xf2w\x10L=\xf9\xbf\x1e\r\xd8\x15\xad\x0c6lF\x96\xbf{\x07\xdb\\AM\x17\x18P\xe2\xcd\xe8\xf0(\x08\x80\xc5\x1b(k\x12\xd72\x93\xf6\xa0\xfb\xb2`\x97\xb5\xc8\x82\xb3'
ciphertext = ciphertext_v2

def oracle(iv, ciphertext):
    time.sleep(0.001)

    try:
        plaintext_padded = cbc_dec(key, iv, ciphertext)
    except ValueError:
        return False

    return valid_pad(plaintext_padded)
