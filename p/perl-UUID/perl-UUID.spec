Name: perl-UUID
Version: 0.24
Release: alt1
Summary: DCE compatible Universally Unique Identifier library for Perl

Group: Development/Perl
License: GPL or Artistic
Url: http://search.cpan.org/~jrm/UUID/UUID.pm

Source: http://search.cpan.org/CPAN/authors/id/J/JR/JRM/UUID-%version.tar.gz

BuildRequires: libuuid-devel perl(Devel/CheckLib.pm) perl(ExtUtils/MakeMaker.pm)

%description
The UUID library is used to generate unique identifiers for objects that
may be accessible beyond the local system. For instance, they could be
used to generate unique HTTP cookies across multiple web servers without
communication between the servers, and without fear of a name clash.
The generated UUIDs can be reasonably expected to be unique within a
system, and unique across all systems, and are compatible with those
created by the Open Software Foundation (OSF) Distributed Computing
Environment (DCE) utility uuidgen.

%prep
%setup -q -n UUID-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/UUID.pm
%perl_vendor_autolib/UUID

%changelog
* Tue Dec 08 2015 Valery Inozemtsev <shrek@altlinux.ru> 0.24-alt1
- initial release
