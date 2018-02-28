# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(App/pod2pdf.pm) perl(CPAN.pm) perl(Carp.pm) perl(Carp/Heavy.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(Errno.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(FileHandle.pm) perl(Filter/Util/Call.pm) perl(IO/Seekable.pm) perl(LWP/Simple.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(PerlIO.pm) perl(Pod/Html.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Sub/Uplevel.pm) perl(Test/Deep.pm) perl(Text/Diff.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl(overload.pm) perl(parent.pm) perl(threads/shared.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Parallel-Scoreboard
Version:        0.07
Release:        alt1_4
Summary:        Scoreboard for monitoring status of many processes
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Parallel-Scoreboard/
Source0:        http://www.cpan.org/authors/id/K/KA/KAZUHO/Parallel-Scoreboard-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Spiffy.pm)
BuildRequires:  perl(Test/Warn.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Base.pm)
BuildRequires:  perl(Test/Base/Filter.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/Builder/Module.pm)

# Run-time deps
BuildRequires: perl(Class/Accessor/Lite.pm)
BuildRequires: perl(Digest/MD5.pm)
BuildRequires: perl(Fcntl.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(HTML/Entities.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(JSON.pm)
BuildRequires: perl(POSIX.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
Source44: import.info


%description
Parallel::Scoreboard is a pure-perl implementation of a process scoreboard.
By using the module it is easy to create a monitor for many worker process,
like the status module of the Apache HTTP server.

%prep
%setup -q -n Parallel-Scoreboard-%{version}

# Remove bundled modules
for f in inc/Test/More.pm inc/File/Temp.pm inc/Spiffy.pm \
    inc/Test/Base.pm inc/Test/Base/Filter.pm \
    inc/Test/Builder.pm inc/Test/Builder/Module.pm \
    inc/Test/Warn.pm; do
  pat=$(echo "$f" | sed 's,/,\\/,g;s,\.,\\.,g')
  rm $f
  sed -i -e "/$pat/d" MANIFEST
done

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_4
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- update to new release by fcimport

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- update to new release by fcimport

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_1
- update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_8
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_7
- import for Sisyphus (required for RT)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_7
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_5
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_5
- fc import

