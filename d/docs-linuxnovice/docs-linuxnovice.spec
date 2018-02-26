%setup_docs_module linuxnovice ru

Name: %packagename
Version: 0.1.2
Release: alt1

License: %gpl2plus
BuildArch: noarch
Url: http://docs.altlinux.ru

Summary: Linux and UNIX novice guide
Summary(ru_RU.KOI8-R): ����������� ����������� ������������ Linux � UNIX

BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses

# replace alt-docs-extras-linuxnovice
Provides: alt-docs-extras-linuxnovice
Obsoletes: alt-docs-extras-linuxnovice

Source: %name-%version.tar

%description
If you never worked in Linux or other UNIX-like systems this book 
will help you understand basic features and main peculiarities of 
these systems. This book is a concise reviewed edition of 
russian translation of "Linux Installation and Getting Started" by 
Matt Walsh and others. This book may be distributed under terms 
of GPL.

%description -l ru_RU.KOI8-R
���� ��� ����� �� ����������� �������� �� � Linux, �� � UNIX, ��� �����
������� ��� ���������������� � ���� �������� � ���� ���������
�������� ��� ���������������� �������� � ������ ������������.
� ����� ����������� ������� ������� ����������� ������ � ���������
�������: ����������� �������� � ����������� ��������� UNIX � Linux.
������ ����� ������������ ����� �����ݣ���� � ������������ ��������
�������� �������� ����� ����� ����� "Linux Installation
and Getting Started" (����. �. � ��. ����������� ��
��������� � ������������� ������� Linux. �.: ������, 1999), ���������
���������� ������ � ������������ ��������� � IPLabs Linux Team. 
������ ����� ���������������� �� �������� GPL.

%prep
%setup

%build
%docs_module_build html index.html

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Mon Jan 25 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- fix formatting (Closes: #18071)

* Mon Sep 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- fixed typo in module description (#17045)

* Wed Apr 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt3
- package renamed: alt-docs-extras-linuxnovice -> docs-linuxnovice
  + added Provides/Obsoletes
- build with rpm-build-docs-experimental:
  + added License file
  + fixed docinfo file
  + modified spec for rpm-build-docs-experimental
- used macro for License tag
- fixed formatting in russian description

* Sun Jun 06 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.1-alt2
- Syntax changed for alt-docs-genextras-0.2

* Thu May 13 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.1-alt1
- initial release


