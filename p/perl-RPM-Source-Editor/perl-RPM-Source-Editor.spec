%define module RPM-Source-Editor
%def_without hashertarbuild

Name: perl-%module
Version: 0.836
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Perl library for src.rpm and spec file editing
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# due to rpmbuild -bE
# Recommends: rpm-build

# Automatically added by buildreq on Wed Nov 06 2010
BuildRequires: perl-devel /usr/bin/pod2man perl-podlators perl-RPM perl(Clone.pm)
# for RPM::Source::Tools
BuildRequires: perl-upstreamwatch perl-DistroMap perl(Pod/Strip.pm)

Obsoletes: hashertarbuild < 0.73
Conflicts: hashertarbuild < 0.73


%description
Perl extension for editing src.RPMs and spec files

%if_with hashertarbuild
%package -n hashertarbuild
Group: Development/Other
Summary: a tool to create source tarballs for hasher
Requires: %name = %version-%release

%description -n hashertarbuild
A tool to create rpm-based source tarballs for hasher.
Sometimes rpmbuild -bs --nodeps does not work due to macros abcent. 
Use hashertarbuild <spec> to create source tarball ready for hasher.
%endif

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

install -m755 -D hashertarbuild %buildroot%_bindir/hashertarbuild
for i in hashertarbuild; do
    pod2man  --name $i --center 'hashertarbuild' --section 1 --release %version $i > $i.1
done

mkdir -p %buildroot%_man1dir
install -m 644 *.1 %buildroot%_man1dir/

mkdir -p %buildroot%_datadir/srpmtools/hooks
install -Dm644 stdheaders.txt %buildroot%_datadir/srpmtools/data/stdheaders.txt

%files
%doc Changes
#doc README
%_bindir/srpm*
%perl_vendor_privlib/RPM*
#perl_vendor_man3dir/*
%dir %_datadir/srpmtools
%dir %_datadir/srpmtools/hooks
%_datadir/srpmtools/data
%_bindir/buildreq-*
%_man1dir/buildreq-*

#files -n hashertarbuild
%_bindir/hashertarbuild
%_man1dir/hashertarbuild*

%changelog
* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.836-alt1
- development release

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.835-alt1
- bugfix release

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.834-alt1
- bugfix release

* Wed Apr 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.833-alt1
- development release

* Wed Apr 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.832-alt1
- development release

* Fri Apr 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.831-alt1
- development release

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.830-alt1
- development release

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.826-alt1
- bugfix release

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.825-alt1
- bugfix release

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.824-alt1
- development release

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.823-alt1
- bugfix release

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.822-alt1
- bugfix release

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.821-alt1
- bugfix release

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.820-alt1
- bugfix release

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.819-alt1
- bugfix release

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.818-alt1
- development release

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.817-alt1
- bugfix release

* Thu Sep 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.816-alt1
- bugfix release

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.815-alt1
- development release

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.814-alt1
- development release

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.813-alt1
- development release

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.812-alt1
- development release

* Wed Aug 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.811-alt1
- development release; new API

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.810-alt1
- bugfix release

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.809-alt1
- development release

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.808-alt1
- bugfix release

* Tue May 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.807-alt1
- bugfix release

* Tue Apr 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.806-alt1
- bugfix release

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.805-alt1
- development release

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.804-alt1
- bugfix release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.803-alt1
- bugfix release

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.802-alt1
- development release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.801-alt1
- added DependencyFilterFactory

* Sun Feb 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.800-alt1
- development release
