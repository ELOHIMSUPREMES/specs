%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/ParseXS.pm) perl(File/Find.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(Scalar/Util.pm) perl(Test/LongString.pm) perl(Test/More.pm) perl(Test/Warn.pm) perl(XSLoader.pm) perl(Sereal/Decoder.pm)
# END SourceDeps(oneline)
%define module_version 3.006
%define module_name Sereal-Encoder
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 3.006
Release: alt1.1
Summary: Fast, compact, powerful binary serialization
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/Y/YV/YVES/Sereal-Encoder-%{version}.tar.gz

%description
This library implements an efficient, compact-output, and feature-rich
serializer using a binary protocol called *Sereal*.
Its sister module the Sereal::Decoder manpage implements a decoder for this format.
The two are released separately to allow for independent and safer upgrading.

The Sereal protocol version emitted by this encoder implementation is currently
protocol version 1.

The protocol specification and many other bits of documentation
can be found in the github repository. Right now, the specification is at
https://github.com/Sereal/Sereal/blob/master/sereal_spec.pod,
there is a discussion of the design objectives in
https://github.com/Sereal/Sereal/blob/master/README.pod, and the output
of our benchmarks can be seen at
https://github.com/Sereal/Sereal/wiki/Sereal-Comparison-Graphs.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/S*
%perl_vendor_autolib/*

%changelog
* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.006-alt1.1
- rebuild with new perl 5.22.0

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 3.006-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 3.005-alt1
- automated CPAN update

* Mon Dec 29 2014 Igor Vlasenko <viy@altlinux.ru> 3.004-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.003-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 3.003-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.002-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 3.001-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- automated CPAN update

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- build for Sisyphus (required for perl update)

