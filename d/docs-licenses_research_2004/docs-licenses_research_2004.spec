%setup_docs_module licenses_research_2004 ru

Name: %packagename
Version: 0.1
Release: alt1

Summary: Licensing mechanics in government projects (copyright)
Summary(ru_RU.KOI8-R): ��������� �������� ���� (���������, �������������) � ������ ��������������� ��������. ���������� ���������� ����������� ��������
License: distributable
Url: http://80.90.67.45/PMS/Public/PublicProjectForm.aspx?projectid=9ae2d67a-79eb-4932-884d-c5f6d1103e13
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3

# replace docs-standard_licenses_2004-kirill
Provides: docs-standard_licenses_2004-kirill
Obsoletes: docs-standard_licenses_2004-kirill

Source: %name-%version.tar

%description
Standard licenses for government IT projects (ru).

%description -l ru_RU.KOI8-R
���������� ������� �������� �� ������������� � ������ ��������������� ���������� ��� "����������� ������ (2002-2010 ����) ����� (���������, �������������. ���������� ������� ����������� ���������� � ���������� � �������� ������� ����������� ���������� ��������������� ����������. � ����������� �������� �� ���������� ���������, ����������� ����������, ����������� �� ��������������� �������� ����������� ��������� ������������� ����� �� ���������� ����� �� �������������. ��� �������� � �������������� ���������� ���� � ��������� ���������������� ���������. ����� ������ �������������� ������������� �������� ������������ �������������� ������������� ���� �� ���������� ��������������� ���������� (�� ����������� �� ��������), ���������� �� ����������� �������������� �����������, ��������� � ������ � ������� �������������� ������������� ����. ������������� ������������ ����������� �� ����������� � ������������� ������.

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
* Sun May 04 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- package renamed: docs-standard_licenses_2004-kirill -> docs-licenses_research_2004
  + added Provides/Obsoletes
- spec modified for rpm-build-docs-experimental

* Fri May 12 2006 Kirill Maslinsky <kirill@altlinux.ru> 060512-alt1
- Initial build for Sisyphus.

