Name: perl-Dancer2
Version: 0.142000
Release: alt1

Summary: Lightweight yet powerful web application framework
Group: Development/Perl
License: perl

Url: %CPAN Dancer2
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(Capture/Tiny.pm) perl(YAML.pm) perl(Pod/Usage.pm) perl(Template/Tiny.pm) perl(Encode.pm) perl(HTTP/Headers.pm) perl(Config/Any.pm) perl(Plack/Request.pm) perl(Module/Build.pm) perl-devel perl(HTTP/Body.pm) perl(MooX/Types/MooseLike.pm) perl(URI/Escape.pm) perl(Role/Tiny.pm) perl(Test/MockTime.pm) perl(Test/Fatal.pm) perl(URI.pm) perl-libwww perl(Pod/Simple.pm) perl(Test/TCP.pm) perl(Digest/SHA.pm) perl(parent.pm) perl(HTTP/Request/Common.pm) perl(Hash/Merge/Simple.pm) perl(Moo/Role.pm) perl(Test/Script.pm) perl(YAML/Any.pm) perl(HTTP/Server/Simple/PSGI.pm) perl(Class/Load.pm) perl(Moo.pm) perl(Template.pm) perl(MIME/Types.pm) perl(HTTP/Date.pm) perl(JSON.pm) perl(Return/MultiLevel.pm) perl(App/Cmd/Setup.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/dancer2
%_man1dir/dancer2.*
%perl_vendor_privlib/Dancer2*
%perl_vendor_privlib/auto/share/dist/*
%doc AUTHORS Changes LICENSE README.md

%changelog
* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.142000-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.141000-alt1
- automated CPAN update

* Tue Sep 17 2013 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build for ALTLinux

