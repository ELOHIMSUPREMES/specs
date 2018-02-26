# Generated File.
%setup_docs_module informatika1 ru
Name: %packagename
Version: 0.1
Release: alt3

Summary: Practical informatics. Part 1
Summary(ru_RU.KOI8-R): ������������ �����������, ����� 1
License: %fdl
Url: http://www.ctc.msiu.ru/materials/Book1/index1.html
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-informatika1-kirill
Provides: docs-informatika1-kirill = 020617-alt3
Obsoletes: docs-informatika1-kirill <= 020617-alt3

Source: %name-%version.tar

%description
Free textbook for course "Informatics and informational technologies". Part 1.

Please note: while viewing this document in Konqueror you might miss the navigation menu;
use another browser like Firefox then.

%description -l ru_RU.KOI8-R
����� �� ��������� ��������, ������������ ������� ��������� �������� ����������������� ������������ ����������� � ������� �������, -- ��� ���������� �������� ���������������� �� ������� � ������������ ����������.  ������ �������� �������� ������ ��� ��������, ��������� ��������� ������� �������, ������������ ���, ��� ��������� ��������� � ��� ������� ��� �������� � ���������� ������������ ������� ��� ������������� ������������ �����������. ��� ���� �������� �������� ��������� ����������� �������� �� ���� �������� ����������������� ������������ �����������. ������ ������� ���������� ����� ���, ��������� � ������ ����� "����������� � �������������� ����������" �  ������������� ������� ������, ������������ ��  2001-2002 ��. ���.

���������: ��� ��������� ������� ��������� � �onqueror �� ������������ ���� ���������.
����������� ������ ������� �������� Firefox.

%prep
%setup

%build
%docs_module_build "html" "index.html"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Wed Apr 02 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt3
- added note to %%description (#12012)
  + in Konqueror you might miss the navigation menu

* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-informatika1-kirill
  + added Provides/Obsoletes

* Fri Jan 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-informatika1-kirill package

* Tue Jun 19 2007 Kirill Maslinsky <kirill@altlinux.ru> 020617-alt3
- update spec 
  + add Obsolotes: alt-docs-extras-informatika
  + update due to new rpm-build-docs

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 020617-alt2.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Thu Nov 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 020617-alt2
- Auto rebuild with new version.

* Mon Oct 24 2005 Kirill Maslinsky <kirill@altlinux.ru> 020617-alt1
- Auto build with new version.

