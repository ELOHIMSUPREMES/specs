%define sound_dir	%_datadir/asterisk/sounds/
%define sound_lang  fr

Name: asterisk-core-sounds-fr-siren7
Summary: sounds for Asterisk
Version: 1.4.25
Release: alt1
License: GPL
Group: System/Servers
BuildArch: noarch
Obsoletes: asterisk-sounds-fr-siren7 < %version-%release 
Conflicts: asterisk-sounds-fr-siren7 
Requires(pre): asterisk-sounds-fr-base

Url: http://downloads.asterisk.org/pub/telephony/sounds/releases/%name-%version.tar.gz

Source: %name-%version.tar

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%sound_dir/%sound_lang
cp -a ./ %buildroot%sound_dir/%sound_lang/
find -type f \
    | grep -v sounds.list \
    | grep -vP '^.\/(CREDITS|LICENSE|CHANGES)' \
	| grep -vP '\.txt$' \
    | sed 's!\.\/\(.*\)!%sound_dir%sound_lang/\1!' \
    > sounds.list

find -mindepth 1 -type d \
    | sed 's!\.\/\(.*\)!%%dir %sound_dir%sound_lang/\1!' \
	>> sounds.list

find -type f \
    | grep -P '^.\/(CREDITS|LICENSE|CHANGES)' \
    | sed 's!\.\/\(.*\)!%%doc \1\n%%exclude %sound_dir%sound_lang/\1!' \
	>> sounds.list

find -type f \
    | grep -P '\.txt$' \
    | sed 's!\.\/\(.*\)!%%doc \1\n%%exclude %sound_dir%sound_lang/\1!' \
	>> sounds.list

%files -f sounds.list

%changelog
* Thu Oct 31 2013 Cronbuild Service <cronbuild@altlinux.org> 1.4.25-alt1
- new version 1.4.25

* Sat Aug 17 2013 Cronbuild Service <cronbuild@altlinux.org> 1.4.24-alt1
- new version 1.4.24

* Fri Jan 11 2013 Cronbuild Service <cronbuild@altlinux.org> 1.4.23-alt1
- new version 1.4.23

* Wed Jan 02 2013 Cronbuild Service <cronbuild@altlinux.org> 1.4.22-alt1
- new version 1.4.22

* Tue Jan 01 2013 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt5
- fix cronbuild support

* Fri Dec 28 2012 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt4
- add watch-file and cronbuild support

* Sat Sep 24 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt3
- add Obsoletes to old sounds packages

* Sun Jul 24 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt2
- add requires to asterisk-sounds-fr-base

* Tue Jul 19 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.21-alt1
- first build


