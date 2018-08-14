# -*- coding: utf-8 -*-
"""
magic.py

 Initial Author: Jason Petrone <jp@demonseed.net>

 Updated by Gabriel Wicke <groups@gabrielwicke.de>
    Thu Oct 16 23:00:03 CEST 2003
    with magic data from gnome-vfs-mime-magic

"""
__version__ = '$Revision: 1.2 $'[11:-2]

import six
import string
import struct


magic = [

    [0, 'string', '=', b'%PDF-', 'application/pdf'],
    [0, 'string', '=', b'\177ELF', 'application/x-executable'],
    [0, 'string', '=', b'\004%!', 'application/postscript'],
    [0, 'string', '=', b'\000\000\001\272', 'video/mpeg'],
    [0, 'string', '=', b'\000\000\001\263', 'video/mpeg'],
    [0, 'string', '=', b'\x47\x3f\xff\x10', 'video/mpeg'],
    [0, 'string', '=', b'\377\330\377', 'image/jpeg'],
    [0, 'string', '=', b'\xed\xab\xee\xdb', 'application/x-rpm'],
    [0, 'string', '=', b'Rar!', 'application/x-rar'],
    [257, 'string', '=', b'ustar\0', 'application/x-tar'],
    [257, 'string', '=', b'ustar\040\040\0', 'application/x-gtar'],
    # the following detection of OOo is according to
    # http://books.evc-cit.info/oobook/ch01.html
    # and some heuristics found in hexeditor. if theres a better way to detect,
    # we should replace the signatures below.
    # best would to just read and evaluate the manifest file of the zip, but
    # the magic tests are running on the first 8kB, so we cant unzip the
    # manifest in files >8kB.
    [30, 'string', '=', b'mimetypeapplication/vnd.sun.xml.writer',
     'application/vnd.sun.xml.writer'],
    [30, 'string', '=', b'mimetypeapplication/vnd.sun.xml.calc',
     'application/vnd.sun.xml.calc'],
    [30, 'string', '=', b'mimetypeapplication/vnd.sun.xml.draw',
     'application/vnd.sun.xml.draw'],
    [30, 'string', '=', b'mimetypeapplication/vnd.sun.xml.impress',
     'application/vnd.sun.xml.impress'],
    [30, 'string', '=', b'mimetypeapplication/vnd.sun.xml.chart',
     'application/vnd.sun.xml.chart'],
    [30, 'string', '=', b'mimetypeapplication/vnd.sun.xml.global',
     'application/vnd.sun.xml.global'],
    # zip works now, after we have it with lower priority than OOo
    [0, 'string', '=', b'PK\003\004', 'application/zip'],
    [0, 'string', '=', b'GIF8', 'image/gif'],
    [4, 'string', '=', b'moov', 'video/quicktime'],
    [4, 'string', '=', b'mdat', 'video/quicktime'],
    [8, 'string', '=', b'mp42', 'video/quicktime'],
    [12, 'string', '=', b'mdat', 'video/quicktime'],
    [36, 'string', '=', b'mdat', 'video/quicktime'],
    [0, 'belong', '=', b'0x3026b275', 'video/x-ms-asf'],
    [0, 'string', '=', b'ASF ', 'audio/x-ms-asx'],
    [0, 'string', '=', b'<ASX', 'audio/x-ms-asx'],
    [0, 'string', '=', b'<asx', 'audio/x-ms-asx'],
    [0, 'string', '=', b'MThd', 'audio/x-midi'],
    [0, 'string', '=', b'IMPM', 'audio/x-it'],
    [2, 'string', '=', b'-lh0-', 'application/x-lha'],
    [2, 'string', '=', b'-lh1-', 'application/x-lha'],
    [2, 'string', '=', b'-lz4-', 'application/x-lha'],
    [2, 'string', '=', b'-lz5-', 'application/x-lha'],
    [2, 'string', '=', b'-lzs-', 'application/x-lha'],
    [2, 'string', '=', b'-lh\40-', 'application/x-lha'],
    [2, 'string', '=', b'-lhd-', 'application/x-lha'],
    [2, 'string', '=', b'-lh2-', 'application/x-lha'],
    [2, 'string', '=', b'-lh3-', 'application/x-lha'],
    [2, 'string', '=', b'-lh4-', 'application/x-lha'],
    [2, 'string', '=', b'-lh5-', 'application/x-lha'],
    [20, 'string', '=', b'\375\304\247\334', 'application/x-zoo'],
    [0, 'string', '=', b'StuffIt ', 'application/x-stuffit'],
    [11,
     'string',
     '=',
     b'must be converted with BinHex',
     'application/mac-binhex40'],
    [102, 'string', '=', b'mBIN', 'application/x-macbinary'],
    [4, 'string', '=', b'gtktalog ', 'application/x-gtktalog'],
    [0, 'string', '=', b'diff ', 'text/x-patch'],
    [0, 'string', '=', b'Index:', 'text/x-patch'],
    [0, 'string', '=', b'*** ', 'text/x-patch'],
    [0, 'string', '=', b'Only in ', 'text/x-patch'],
    [0, 'string', '=', b'Common subdirectories: ', 'text/x-patch'],
    [0, 'string', '=', b'FONT', 'application/x-font-vfont'],
    [0, 'string', '=', b'IIN1', 'image/tiff'],
    [0, 'string', '=', b'MM\x00\x2a', 'image/tiff'],
    [0, 'string', '=', b'II\x2a\x00', 'image/tiff'],
    [0, 'string', '=', b'\x89PNG', 'image/png'],
    [0,
     'string',
     '=',
     b'8BPS\ \ \000\000\000\000 &0xffffffff0000ffffffff',
     'image/x-psd'],
    [0, 'string', '=', b'#LyX', 'text/x-lyx'],
    [0, 'string', '=', b'DCMw', 'application/dicom'],
    [0, 'string', '=', b'gimp xcf', 'image/x-xcf'],
    [0, 'belong', '=', b'0x59a66a95', 'image/x-sun-raster'],
    [0, 'belong', '=', b'0x01da0000 &0xfcfeffff', 'image/x-sgi'],
    [0, 'belong', '=', b'0xb168de3a', 'image/x-pcx'],
    [0, 'string', '=', b'\x28\x00\x00\x00', 'image/x-dib'],
    [0, 'string', '=', b'SIMPLE  =', 'image/x-fits'],
    [0, 'belong', '=', b'0x46506978', 'image/x-fpx'],
    [0, 'belong', '=', b'0x00000200', 'image/x-icb'],
    [0, 'belong', '=', b'0x53445058', 'image/dpx'],
    [0, 'string', '=', b'[Desktop Entry]', 'application/x-gnome-app-info'],
    [0, 'string', '=', b'[X-GNOME-Metatheme]', 'application/x-gnome-theme'],
    [0,
     'string',
     '=',
     b'<nautilus_object nautilus_link',
     'application/x-nautilus-link'],
    [0, 'string', '=', b'URL:', 'application/x-gmc-link'],
    [0, 'string', '=', b'/* XPM */', 'image/x-xpixmap'],
    [0, 'string', '=', b'<!DOCTYPE xbel', 'application/xbel'],
    [0, 'string', '=', b'<xbel', 'application/xbel'],
    [0,
     'string',
     '=',
     b'<!DOCTYPE NETSCAPE-Bookmark-file-1\>',
     'application/x-mozilla-bookmarks'],
    [0,
     'string',
     '=',
     b'<!DOCTYPE NETSCAPE-Bookmark-file-1\>',
     'application/x-netscape-bookmarks'],
    [0,
     'string',
     '=',
     b'<ephy_bookmarks        ',
     'application/x-epiphany-bookmarks'],
    [0, 'string', '=', b'<!DOCTYPE svg', 'image/svg+xml'],
    [0, 'string', '=', b'<svg', 'image/svg+xml'],
    [0, 'string', '=', b'<?php', 'application/x-php'],
    [0, 'string', '=', b'<smil\>', 'application/smil'],
    [0, 'string', '=', b'<SMIL\>', 'application/smil'],
    [0, 'string', '=', b'<!DOCTYPE HTML', 'text/html'],
    [0, 'string', '=', b'<!DOCTYPE html', 'text/html'],
    [0, 'string', '=', b'<!doctype html', 'text/html'],
    [0, 'string', '=', b'<!doctype Html', 'text/html'],
    [0, 'string', '=', b'<!doctype HTML', 'text/html'],
    [10, 'string', '=', b'<HEAD', 'text/html'],
    [10, 'string', '=', b'<head', 'text/html'],
    [16, 'string', '=', b'<TITLE', 'text/html'],
    [16, 'string', '=', b'<title', 'text/html'],
    [10, 'string', '=', b'<html', 'text/html'],
    [0, 'string', '=', b'<HTML', 'text/html'],
    [0, 'string', '=', b'<dia:diagram', 'application/x-dia-diagram'],
    [0, 'string', '=', b'<abiword', 'application/x-abiword'],
    [0, 'string', '=', b'<\!DOCTYPE abiword', 'application/x-abiword'],
    [0, 'string', '=', b'gmr:Workbook', 'application/x-gnumeric'],
    [0, 'string', '=', b'<?xml', 'text/xml'],
    [0, 'string', '=', b'{\\rtf', 'application/rtf'],
    [0, 'string', '=', b'#!/bin/sh', 'text/x-sh'],
    [0, 'string', '=', b'#!/bin/bash', 'text/x-sh'],
    [0, 'string', '=', b'#!/bin/csh', 'text/x-csh'],
    [0, 'string', '=', b'#!/bin/ksh', 'application/x-shellscript'],
    [0, 'string', '=', b'#!/bin/perl', 'text/x-perl'],
    [0, 'string', '=', b'#!/bin/zsh', 'application/x-shellscript'],
    [1, 'string', '=', b'/bin/sh', 'text/x-sh'],
    [1, 'string', '=', b'/bin/bash', 'text/x-sh'],
    [1, 'string', '=', b'/bin/csh', 'text/x-csh'],
    [1, 'string', '=', b'/bin/ksh', 'application/x-shellscript'],
    [1, 'string', '=', b'/bin/perl', 'text/x-perl'],
    [0, 'string', '=', b'BEGIN:VCARD', 'text/x-vcard'],
    [0, 'string', '=', b'BEGIN:VCALENDAR', 'text/calendar'],
    [8, 'string', '=', b'CDR vrsn', 'application/vnd.corel-draw'],
    [8, 'string', '=', b'AVI ', 'video/x-msvideo'],
    [0, 'string', '=', b'MOVI', 'video/x-sgi-movie'],
    [0, 'string', '=', b'.snd', 'audio/basic'],
    [8, 'string', '=', b'AIFC', 'audio/x-aifc'],
    [8, 'string', '=', b'AIFF', 'audio/x-aiff'],
    [0, 'string', '=', b'.ra\375', 'audio/vnd.rn-realaudio'],
    [0, 'belong', '=', b'0x2e7261fd', 'audio/vnd.rn-realaudio'],
    [0, 'string', '=', b'.RMF', 'audio/x-pn-realaudio'],
    [8, 'string', '=', b'WAVE', 'audio/x-wav'],
    [8, 'string', '=', b'WAV ', 'audio/x-wav'],
    [0, 'string', '=', b'ID3', 'audio/mpeg'],
    [0, 'string', '=', b'0xfff0', 'audio/mpeg'],
    [0, 'string', '=', b'\x00\x00\x01\xba', 'video/mpeg'],
    [8, 'string', '=', b'CDXA', 'video/mpeg'],
    [0, 'belong', '=', b'0x000001ba', 'video/mpeg'],
    [0, 'belong', '=', b'0x000001b3', 'video/mpeg'],
    [0, 'string', '=', b'RIFF', 'audio/x-riff'],
    [0, 'string', '=', b'OggS   ', 'audio/ogg'],
    [0, 'string', '=', b'pnm:\/\/', 'audio/vnd.rn-realaudio'],
    [0, 'string', '=', b'rtsp:\/\/', 'audio/vnd.rn-realaudio'],
    [0, 'string', '=', b'SIT!', 'application/x-stuffit'],
    [0, 'string', '=', b'\312\376\272\276', 'application/x-java'],
    [0, 'string', '=', b'Joy!', 'application/x-pef-executable'],
    [4, 'string', '=', b'\x11\xAF', 'video/x-flic'],
    [4, 'string', '=', b'\x12\xAF', 'video/x-flic'],
    [0, 'string', '=', b'\x31\xbe\x00\x00', 'application/msword'],
    [0, 'string', '=', b'PO^Q`', 'application/msword'],
    [0, 'string', '=', b'\376\067\0\043', 'application/msword'],
    [0, 'string', '=', b'\320\317\021\340\241\261', 'application/msword'],
    [0, 'string', '=', b'\333\245-\0\0\0', 'application/msword'],
    [0,
     'string',
     '=',
     b'Microsoft Excel 5.0 Worksheet',
     'application/vnd.ms-excel'],
    [0, 'string', '=', b'Biff5', 'application/vnd.ms-excel'],
    [0,
     'string',
     '=',
     b'*BEGIN SPREADSHEETS    ',
     'application/x-applix-spreadsheet'],
    [0,
     'string',
     '=',
     b'*BEGIN SPREADSHEETS    ',
     'application/x-applix-spreadsheet'],
    [0, 'string', '=', b'\x00\x00\x02\x00', 'application/vnd.lotus-1-2-3'],
    [0, 'belong', '=', b'0x00001a00', 'application/vnd.lotus-1-2-3'],
    [0, 'belong', '=', b'0x00000200', 'application/vnd.lotus-1-2-3'],
    [0, 'string', '=', b'PSID', 'audio/prs.sid'],
    [31, 'string', '=', b'Oleo', 'application/x-oleo'],
    [0, 'string', '=', b'FFIL', 'application/x-font-ttf'],
    [65, 'string', '=', b'FFIL', 'application/x-font-ttf'],
    [0, 'string', '=', b'LWFN', 'application/x-font-type1'],
    [65, 'string', '=', b'LWFN', 'application/x-font-type1'],
    [0, 'string', '=', b'StartFont', 'application/x-font-sunos-news'],
    [0, 'string', '=', b'\x13\x7A\x29', 'application/x-font-sunos-news'],
    [8, 'string', '=', b'\x13\x7A\x2B', 'application/x-font-sunos-news'],
    [0, 'string', '=', b'%!PS-AdobeFont-1.', 'application/x-font-type1'],
    [6, 'string', '=', b'%!PS-AdobeFont-1.', 'application/x-font-type1'],
    [0, 'string', '=', b'%!FontType1-1.', 'application/x-font-type1'],
    [6, 'string', '=', b'%!FontType1-1.', 'application/x-font-type1'],
    [0, 'string', '=', b'STARTFONT\040', 'application/x-font-bdf'],
    [0, 'string', '=', b'\001fcp', 'application/x-font-pcf'],
    [0, 'string', '=', b'D1.0\015', 'application/x-font-speedo'],
    [0, 'string', '=', b'\x14\x02\x59\x19', 'application/x-font-libgrx'],
    [0, 'string', '=', b'\xff\x46\x4f\x4e', 'application/x-font-dos'],
    [7, 'string', '=', b'\x00\x45\x47\x41', 'application/x-font-dos'],
    [7, 'string', '=', b'\x00\x56\x49\x44', 'application/x-font-dos'],
    [0, 'string', '=', b'\<MakerScreenFont', 'application/x-font-framemaker'],
    [0, 'string', '=', b'\000\001\000\000\000', 'application/x-font-ttf'],
    [1, 'string', '=', b'WPC', 'application/x-wordperfect'],
    [0, 'string', '=', b'ID;', 'text/spreadsheet'],
    [0, 'string', '=', b'MZ', 'application/x-ms-dos-executable'],
    [0, 'string', '=', b'%!', 'application/postscript'],
    [0, 'string', '=', b'BZh', 'application/x-bzip'],
    [0, 'string', '=', b'\x1f\x8b', 'application/x-gzip'],
    [0, 'string', '=', b'\037\235', 'application/x-compress'],
    [0, 'string', '=', b'\367\002', 'application/x-dvi'],
    [0, 'string', '=', b'\367\203', 'application/x-font-tex'],
    [0, 'string', '=', b'\367\131', 'application/x-font-tex'],
    [0, 'string', '=', b'\367\312', 'application/x-font-tex'],
    [2, 'string', '=', b'\000\022', 'application/x-font-tex-tfm'],
    [0, 'string', '=', b'\x36\x04', 'application/x-font-linux-psf'],
    [0, 'string', '=', b'FWS', 'application/x-shockwave-flash'],
    [0, 'string', '=', b'CWS', 'application/x-shockwave-flash'],
    [0, 'string', '=', b'NSVf', 'video/x-nsv'],
    [0, 'string', '=', b'BMxxxx\000\000 &0xffff00000000ffff', 'image/bmp'],
    [0, 'string', '=', b'Return-Path:', 'message/rfc822'],
    [0, 'string', '=', b'Path:', 'message/news'],
    [0, 'string', '=', b'Xref:', 'message/news'],
    [0, 'string', '=', b'From:', 'message/rfc822'],
    [0, 'string', '=', b'Received:', 'message/rfc822'],
    [0, 'string', '=', b'[playlist]', 'audio/x-scpls'],
    [0, 'string', '=', b'[Reference]', 'video/x-ms-asf'],
    [0, 'string', '=', b'fLaC', 'application/x-flac'],
    [32769, 'string', '=', b'CD001', 'application/x-cd-image'],
    [37633, 'string', '=', b'CD001', 'application/x-cd-image'],
    [32776, 'string', '=', b'CDROM', 'application/x-cd-image'],
    [0, 'string', '=', b'OTTO', 'application/x-font-otf'],
    [54, 'string', '=', b'S T O P', 'application/x-ipod-firmware'],
    [0, 'string', '=', b'BLENDER', 'application/x-blender'],
    [0, 'string', '=', b'import ', 'text/x-python'],
]

magicNumbers = []


def strToNum(n):
    val = 0
    col = 1
    if n[:1] == 'x':
        n = '0' + n
    if n[:2] == '0x':
        # hex
        n = n[2:].lower()
        while len(n) > 0:
            l = n[len(n) - 1]
            val = val + string.hexdigits.index(l) * col
            col = col * 16
            n = n[:len(n) - 1]
    elif n[0] == '\\':
        # octal
        n = n[1:]
        while len(n) > 0:
            l = n[len(n) - 1]
            if ord(l) < 48 or ord(l) > 57:
                break
            val = val + int(l) * col
            col = col * 8
            n = n[:len(n) - 1]
    else:
        val = int(n)
    return val


class magicTest:

    def __init__(self, offset, t, op, value, msg, mask=None):
        # XXX: ``mask`` not used inside this package. Check wether used from
        #      outside somewhere in plone. If so, write test, else remove.
        if t.count('&') > 0:
            mask = strToNum(t[t.index('&') + 1:])
            t = t[:t.index('&')]
        if isinstance(offset, type('a')):
            self.offset = strToNum(offset)
        else:
            self.offset = offset
        self.type = t
        self.msg = msg
        self.subTests = []
        self.op = op
        self.mask = mask
        self.value = value

    def test(self, data):
        if self.mask:
            # XXX: never reached in test, ever needed/used?
            data = data & self.mask
        if self.op == '=':
            if self.value == data:
                return self.msg
        elif self.op == '<':
            # XXX: not implemented, not used, remove?
            pass
        elif self.op == '>':
            # XXX: not implemented, not used, remove?
            pass
        elif self.op == '&':
            # XXX: not implemented, not used, remove?
            pass
        elif self.op == '^':
            # XXX: not implemented, not used, remove?
            pass
        return None

    def compare(self, data):
        try:
            if self.type == 'string':
                c = b''
                s = b''
                for i in range(0, len(self.value) + 1):
                    if i + self.offset > len(data) - 1:
                        break
                    s = s + c
                    d = data[self.offset + i]
                    d = d if six.PY2 else bytes([d])
                    [c] = struct.unpack('c', d)
                data = s
            elif self.type == 'short':
                # XXX: not used inside this package. Check wether used from
                #      outside somewhere in plone. If so, write test, else remove.
                [data] = struct.unpack('h', data[self.offset:self.offset + 2])
            elif self.type == 'leshort':
                # XXX: not used inside this package. Check wether used from
                #      outside somewhere in plone. If so, write test, else remove.
                [data] = struct.unpack('<h', data[self.offset:self.offset + 2])
            elif self.type == 'beshort':
                # XXX: not used inside this package. Check wether used from
                #      outside somewhere in plone. If so, write test, else remove.
                [data] = struct.unpack('>H', data[self.offset:self.offset + 2])
            elif self.type == 'long':
                # XXX: not used inside this package. Check wether used from
                #      outside somewhere in plone. If so, write test, else remove.
                [data] = struct.unpack('l', data[self.offset:self.offset + 4])
            elif self.type == 'lelong':
                # XXX: not used inside this package. Check wether used from
                #      outside somewhere in plone. If so, write test, else remove.
                [data] = struct.unpack('<l', data[self.offset:self.offset + 4])
            elif self.type == 'belong':
                [data] = struct.unpack('>l', data[self.offset:self.offset + 4])
            else:
                pass
        except:
            return None

        return self.test(data)


def guessMime(data):
    for test in magicNumbers:
        m = test.compare(data)
        if m:
            return m
    # no matching, magic number.
    return

for m in magic:
    magicNumbers.append(magicTest(m[0], m[1], m[2], m[3], m[4]))
