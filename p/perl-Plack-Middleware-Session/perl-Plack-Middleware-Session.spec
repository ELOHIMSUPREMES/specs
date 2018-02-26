Name: perl-Plack-Middleware-Session
Version: 0.15
Release: alt1
Summary: Plack::Middleware::Session - Middleware for session management

Group: Development/Perl
License: Perl
Url: %CPAN Plack-Middleware-Session

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Plack perl-Test-Fatal perl-Test-Requires perl-Digest-SHA1 perl-Module-Install perl-Digest-HMAC

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Plack/Middleware/Session*
%perl_vendor_privlib/Plack/Session*
%doc Changes README 

%changelog
* Sun Sep 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- 0.14 -> 0.15

* Fri Jul 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- initial build
