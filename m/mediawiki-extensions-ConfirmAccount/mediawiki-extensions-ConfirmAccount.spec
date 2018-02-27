%define oname ConfirmAccount
%define major 1.20
%define dversion MW%major
%define revision 83ae0c9

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: This extension disables direct account creation and requires submission and approval.

Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.20

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://codeload.github.com/wikimedia/mediawiki-extensions-ConfirmAccount/legacy.tar.gz/REL1_20
Source: %oname-%version.tar

%description
The ConfirmAccount extension disables direct account creation
and requires submission and approval of accounts by bureaucrats.
Account creations can be enabled through configuring user rights,
such as if you wanted Sysops/Bureaucrats to be able to directly make them.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Wed Jul 24 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20.83ae0c9-alt1
- new version (1.20.83ae0c9)

* Sun Aug 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.16.r62787-alt2
- rename spec
- fixes for MW > 1.16

* Sun Aug 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.16.r62787-alt1
- new version (1.16.r62787) import in git

