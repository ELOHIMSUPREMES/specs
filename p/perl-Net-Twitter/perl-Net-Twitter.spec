Name: perl-Net-Twitter
Version: 4.01006
Release: alt1

Summary: A perl interface to the Twitter API
Group: Development/Perl
License: perl

Url: %CPAN Net-Twitter
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(DateTime.pm) perl(DateTime/Format/Strptime.pm) perl(Encode.pm) perl(Digest/SHA.pm) perl(Module/Build.pm) perl(Net/OAuth.pm) perl(Moose/Role.pm) perl(Try/Tiny.pm) perl(Devel/StackTrace.pm) perl(Net/Netrc.pm) perl(Net/OAuth/Message.pm) perl(Moose/Exporter.pm) perl(HTTP/Request/Common.pm) perl-devel perl(HTTP/Response.pm) perl(Data/Visitor/Callback.pm) perl(URI/Escape.pm) perl(Test/Fatal.pm) perl(LWP/Protocol/https.pm) perl(HTML/Entities.pm) perl(Moose.pm) perl(Net/HTTP.pm) perl(URI.pm) perl(namespace/autoclean.pm) perl(Class/Load.pm) perl(Moose/Meta/Method.pm) perl(Test/Warn.pm) perl-libwww perl(Carp/Clan.pm) perl(MooseX/Role/Parameterized.pm) perl(JSON.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/Twitter*
%perl_vendor_privlib/Net/Identica.pm
%doc Changes LICENSE README

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.01006-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 4.01004-alt1
- automated CPAN update

* Wed Jan 15 2014 Vladimir Lettiev <crux@altlinux.ru> 4.01000-alt1
- initial build for ALTLinux

