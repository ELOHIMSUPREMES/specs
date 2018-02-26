%define dist Pod-Perldoc
Name: perl-%dist
Version: 3.17
Release: alt1

Summary: perldoc is program for reading Pod documentation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Pod::Perldoc frontends require additional modules
%add_findreq_skiplist */Pod/Perldoc/ToTk.pm
%add_findreq_skiplist */Pod/Perldoc/ToRtf.pm
%add_findreq_skiplist */Pod/Perldoc/ToXml.pm

BuildArch: noarch

Provides: perldoc = %version
Obsoletes: perldoc < %version

Requires: groff-base less

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: less perl-devel perl-parent perl-podlators

%description
perldoc is program for reading Pod documentation.  Pod (the Plain
Old Documentation format) is a simple-to-use markup language used
for writing documentation for Perl, Perl programs, and Perl modules.

%prep
%setup -q -n %dist-%version

# disable build dependency on Tk::Pod
%ifdef __buildreqs
sed -i- 's/require Tk;/die;/' t/load.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
	%_bindir/perldoc
	%perl_vendor_privlib/Pod
# XXX perl-pod has pod/perldoc.pod
%doc	%perl_vendor_privlib/perldoc.pod

%changelog
* Tue Sep 25 2012 Alexey Tourbin <at@altlinux.ru> 3.17-alt1
- 3.15 -> 3.17
- renamed perldoc packages to perl-Pod-Perldoc

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 3.15-alt1
- new version 3.15
- dropped patches (Closes: #9043)
- rebuilt with perl 5.12

* Fri Apr 22 2005 Alexey Tourbin <at@altlinux.ru> 3.14-alt2
- implemented cache for nroff formatted output (mkdir ~/.perldoc)

* Thu Dec 09 2004 Alexey Tourbin <at@altlinux.ru> 3.14-alt1
- initial revision (split off from perl-base)
