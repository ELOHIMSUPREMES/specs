Name:		refal-plus
Version:	2412
Release:	alt1
Summary:	A modern dialect of Refal programming language
Summary(ru_RU.KOI8-R): ����������� ������� ����� ���������������� �����
Source:		refal-r%{version}-src.zip
Source1:	http://wiki.botik.ru/twiki/pub/Refaldevel/Download/RefalPlusReferenceManual.pdf
Patch:		refal-r2412.patch
License:	GPLv2
Group:		Development/Functional
URL:		http://rfp.botik.ru/

# Automatically added by buildreq on Tue Sep 28 2010
BuildRequires: gcc-c++ libgmp-devel unzip

%description
Refal Plus is a modern dialect of Refal programming language.

Refal (REcursive Functions Algorithmic Language) was originally
developed in the middle of 1960s by V.F.Turchin as a tool for describing
the semantics of other algorithmic languages. Later, when reasonably
efficient Refal implementations had been created, Refal was used as
a symbol manipulation language in such fields as computer algebra,
compiler and interpreter writing, artificial intelligence, etc.

The principal data type in Refal are arbitrary trees, referred to as
ground expressions. In programs and text files ground expressions are
represented by linear sequences of symbols and parentheses, with
parentheses being properly paired. Symbols represent such elementary
data objects as characters, words, numbers and references to objects.

The principal means of analyzing and accessing ground expressions is
pattern matching. Refal patterns may contain symbols, parentheses, and
variables. If matching a ground expression against a pattern succeeds,
the pattern's variables are bound to the corresponding components of the
ground expression, which can be used later for building new ground
expressions.

Refal Plus has been developed taking into account the experience gained
from the design, implementation and use of such languages as Basic
Refal, Refal-2, Refal-4, Refal-5 and RL.

As compared to the other Refal dialects, Refal Plus provides the
following features:

    * Advanced modules support
    * Static declarations of dynamic objects
    * Significantly improved function declarations
    * Failure and error trapping
    * Input/output of ground expressions
    * Operations on boxes, vectors, and tables
    * "Vector" representation of ground expressions

%description -l ru_RU.KOI8-R
����� ���� ������������ ����� ���� �� ��������� ����� ����������������
�����.

����� (��������������� ���� ����������� �������) ��� ������ �.�.��������
� �������� �����, ���������������� ��� �������� ��������� ������
��������������� ������ [��� 66], [��� 71]. ������������, ����� ���������
���������� ����������� ���������� [��� 72], [��� 77], [��� 87�] �����
����� ���������� � ����� �������� ��� ������������ �������,
��������������� ������������ � ���������������, ������������� ���������
� ��.

�������� ����� ������ � ������ �������� ��������� ���������, �������
������������ ����� ������������ �������, ������������ � �������� ������
��� ������������������ �������� � ������ ��������� �����������
������������ ������. ������� ������������ ����� ������������ �������
(����� ��� ������, �����, ����� � ������ �� �������).

�������� ��������� ��� ������� ��������� ��������� ��������� � ���
������� � �� ����������� �������� ������������� � ��������. �������
� ������ ����� ��������� �������, ������ � ����������. ���� ���������
��������� ����� ��������� ��������������� �������, ����������, ��������
� �������, �������� � �������� �������� ��������� ���������� ���������.
�������� ���������� ������������ ����� �������������� ��� ����������
����� ��������� ���������.

�����-��������� ������������ ����� ����� ����������� �������. ������
������� �������� � �������� ��������� ��������� ��������� ���������
� ������������ � �������� ���������� ��������� ��������� ���������.
������� ����� ������������ ������� �������� ���� �����. ��������
��������� ����������� ���������� � ���������� �������� ��������, �.�.
����� ���������� ������� ������� ��� ������� ��������� ������� ��������
���� ���� (���� ���������������, ���� ����� ������ �������).

����� ���� ������ � ���������� ��������� �����, ������������ ���
����������, ���������� � ������������� ��������� ������ [��� 77],
������-2 [��� 86], [��� 87], [��� 87�], ������-4 [��� 87�], [��� 87�],
������-5 [��� 89], � ������ FLAC [��� 87] � RL [��� 87�], [��� 88�],
[��� 88�].

%package devel
Group:		Development/C
Summary:	Development suite for C/C++ programming with %name

%description devel
Development suite for %name

%package samples
Group:		Development/Functional
Summary:	Sample applications for %name

%description samples
Sample applications for %name

%prep
%setup -n refal-r%{version}-src
%patch -p1
touch c++/rules.mk

%build
cp %SOURCE1 .
# Time in the future bug?
find . -exec touch {} \;
cd c++
./configure -prefix /usr
%make_build

%install
cd c++
%makeinstall INSTALL_DIR=%buildroot%_prefix
%ifarch x86_64
mkdir %buildroot%_libdir
mv %buildroot%_prefix/lib/lib* %buildroot%_libdir/
%endif

%files
%doc doc AUTHORS ChangeLog Developers README *.pdf
%_bindir/*
%dir %_prefix/lib/%name
%_prefix/lib/%name/*

%files devel
%_libdir/lib*
%_includedir/*

%files samples
%doc compiler rfp rfpfilt samples trefal

%changelog
* Tue Sep 28 2010 Fr. Br. George <george@altlinux.ru> 2412-alt1
- Initial build from scratch

