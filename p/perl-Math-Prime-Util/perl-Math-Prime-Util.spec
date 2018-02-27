%define _unpackaged_files_terminate_build 1
%define module_version 0.43
%define module_name Math-Prime-Util
%add_findreq_skiplist %perl_vendor_archlib/Math/Prime/Util.pm
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Benchmark.pm) perl(Bytes/Random/Secure.pm) perl(Carp.pm) perl(Config.pm) perl(Crypt/Primes.pm) perl(Crypt/Random.pm) perl(Data/BitStream/XS.pm) perl(Data/Dump.pm) perl(Devel/Size.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec/Functions.pm) perl(FindBin.pm) perl(Iterator/Simple.pm) perl(List/Util.pm) perl(Math/BigFloat.pm) perl(Math/BigInt.pm) perl(Math/Factor/XS.pm) perl(Math/MPFR.pm) perl(Math/Pari.pm) perl(Math/PariInit.pm) perl(Math/Primality.pm) perl(Math/Prime/XS.pm) perl(Term/ANSIColor.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Text/Diff.pm) perl(Tie/Array.pm) perl(Time/HiRes.pm) perl(XSLoader.pm) perl(autodie.pm) perl(base.pm) perl(bigint.pm) perl(bignum.pm) perl(constant.pm) perl(threads.pm) perl(threads/shared.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.43
Release: alt1
Summary: Utilities related to prime numbers, including fast sieves and factoring
Group: Development/Perl
License: perl
URL: https://github.com/danaj/Math-Prime-Util

Source: http://www.cpan.org/authors/id/D/DA/DANAJ/Math-Prime-Util-%{version}.tar.gz

%description
A set of utilities related to prime numbers.  These include multiple sieving.methods, is_prime, prime_count, nth_prime, approximations and bounds for
the prime_count and nth prime, next_prime and prev_prime, factoring utilities,
and more.

The default sieving and factoring are intended to be (and currently are)
the fastest on CPAN, including the Math::Prime::XS manpage, the Math::Prime::FastSieve manpage,
the Math::Factor::XS manpage, the Math::Prime::TiedArray manpage, the Math::Big::Factors manpage,
the Math::Factoring manpage, and the Math::Primality manpage (when the GMP module is available).
For numbers in the 10-20 digit range, it is often orders of magnitude faster.
Typically it is faster than the Math::Pari manpage for 64-bit operations.

All operations support both Perl UV's (32-bit or 64-bit) and bignums.  It
requires no external software for big number support, as there are Perl
implementations included that solely use Math::BigInt and Math::BigFloat.
If you want high performance with big numbers (larger than Perl's UV
size), you should install the Math::Prime::Util::GMP manpage.  This will be a
recurring theme throughout this documentation -- while all bignum operations
are supported in pure Perl, most methods will be much slower than the C+GMP
alternative.

The module is thread-safe and allows concurrency between Perl threads while
still sharing a prime cache.  It is not itself multi-threaded.  See the
Limitations section if you are using Win32 and threads in
your program.

Two scripts are also included and installed by default:

=over 4

=item *

primes.pl displays primes between start and end values or expressions,
with many options for filtering (e.g. twin, safe, circular, good, lucky,
etc.).  Use `--help' to see all the options.

=item *

factor.pl operates similar to the GNU `factor' program.  It supports
bigint and expression inputs.

=back

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
%doc Changes LICENSE TODO README examples
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%files scripts
%_bindir/*

%changelog
* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- regenerated from template by package builder

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- initial import by package builder

