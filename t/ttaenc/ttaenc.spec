Name: ttaenc
Version: 3.4.1
Release: alt3.qa1
Summary: The True Audio (TTA) codec lossless audio compressor
Summary(uk_UA.CP1251): ����������� ������������� ������ TTA (The True Audio)
Summary(ru_RU.CP1251): ��������������� ��� ������ ������ TTA (The True Audio)
License: %gpl2only
Group: Sound
URL: http://tta.sourceforge.net/
Source: %name-%version-src.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

%description
The True Audio (TTA) codec is a free, simple, realtime lossless audio
compressor. Based on adaptive prognostic filters, TTA has compared
favorably to a majority of its popular open-source peers. The codec was
built to offer adequate compression levels while maintaining high
operation speeds.

TTA performs lossless compression on multichannel 8,16 and 24 bits data
of the Wav audio files. Being "lossless" means that no data-quality is
lost in the compression - when uncompressed, the data will be identical
to the original. The compression ratios of TTA depend on the type of
music file being compressed, but the compression size will generally
range between 30%% - 70%% of the original. TTA format supports both of
ID3v1/v2 and APEv2 tags.

%description -l uk_UA.CP1251
The True Audio (TTA) ����� - ������, �������, ����������� ����-
��������� ��������� ����. ��������� �� ���������� �������������
��������, TTA ����� ������� ����� ������� ���� ���������� ������� �
�������� �����. ����� ���� ����������, ��� ������������� ��������
��� ���������, ���������� ����� ����������������.

TTA ������ ��������� ��� ����� ��������������� 8, 16 �� 24-������
����� ����-����� WAV. "��� �����" ������, �� �� �����������
���������� ����� ��� �������� ����� - ���������� ��� ������
�������� ��������. ���������� ��������� TTA �������� �� ���� ������ �
�������� ��������� 30%% - 70%% �� ���������. TTA-������ �������
ID3v1/v2 �� APEv2 ����.

%description -l ru_RU.CP1251
The True Audio (TTA) ����� - ���������, ������� �����-���������� ���
������ ��������� �������. ���������� �� ���������� ������������
��������, TTA ������ ��������� � ���� � ������������ ��� ����������
�������� � �������� �����. ����� ��� ����������, ����� ����������
���������� ������ ������, �������� ������� �������� ��������.

TTA ��������� ������ ��� ������ �������������� 8, 16 � 24-�������
������ �����-������ WAV. "��� ������" ��������, ��� �� ��������
�������� ������ ��� ������ - ������������� ������ ����� ���������
����������. ������� ������ TTA ������� �� ���� ������ � ������
���������� 30%% - 70%% �� ���������. TTA-������ ������������ ID3v1/v2 �
APEv2 ����.


%prep
%setup -n %name-%version-src
%patch -p1


%build
%define _optlevel 3
%make_build


%install
install -D -m 0755 %name %buildroot%_bindir/%name


%files
%doc README ChangeLog*
%_bindir/*


%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.4.1-alt3.qa1
- NMU: rebuilt for debuginfo.

* Sun Feb 15 2009 Led <led@altlinux.ru> 3.4.1-alt3
- cleaned up CFLAGS

* Sun Oct 12 2008 Led <led@altlinux.ru> 3.4.1-alt2
- fixed License

* Sat Sep 01 2007 Led <led@altlinux.ru> 3.4.1-alt1
- 3.4.1:
  + added support for standard input/output interface
  + fixed x86_64 build
- updated %%description

* Mon Nov 06 2006 Led <led@altlinux.ru> 3.3-alt3
- fixed x86_64 build
- fixed description formatting

* Tue Feb 14 2006 Led <led@altlinux.ru> 3.3-alt2
- uk and ru descriptions
- fix spec

* Wed Feb 01 2006 Led <led@altlinux.ru> 3.3-alt1
- initial build
