%define _unpackaged_files_terminate_build 1
%define module_version 0.35
%define module_name Reply
# BEGIN SourceDeps(oneline):
BuildRequires: perl(App/Nopaste.pm) perl(B/Keywords.pm) perl(Carp/Always.pm) perl(Class/Refresh.pm) perl(Config/INI/Reader/Ordered.pm) perl(Data/Dump.pm) perl(Data/Dumper.pm) perl(Data/Printer.pm) perl(Devel/LexAlias.pm) perl(Eval/Closure.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Find.pm) perl(File/HomeDir.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(Getopt/Long.pm) perl(MRO/Compat.pm) perl(Module/Runtime.pm) perl(Package/Stash.pm) perl(PadWalker.pm) perl(Proc/InvokeEditor.pm) perl(Scalar/Util.pm) perl(Term/ANSIColor.pm) perl(Term/ReadLine.pm) perl(Test/More.pm) perl(Time/HiRes.pm) perl(Try/Tiny.pm) perl(base.pm) perl(mro.pm) perl(overload.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.35
Release: alt1
Summary: read, eval, print, loop, yay!
Group: Development/Perl
License: mit
URL: http://metacpan.org/release/Reply

Source: http://www.cpan.org/authors/id/D/DO/DOY/Reply-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc LICENSE README Changes
%perl_vendor_privlib/R*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.34-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- initial import by package builder

