%define module fedora-rawhide-altlinux-sisyphus

Name: distromap-%module
Version: 0.400
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

Requires: distromap-generic-default-altlinux-sisyphus
Requires: distrodb-static-altlinux-sisyphus

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distromap/fedora/rawhide/altlinux/sisyphus
for type in binary source ; do
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
done
ln -s rawhide %buildroot/usr/share/distromap/fedora/default
for type in binary source ; do
	for flag in flags/$type/* ; do
		install -m755 -d $destdir/$flag
		install -m644 $flag/* $destdir/$flag/
	done
done

%files
/usr/share/distromap/*

%changelog
* Wed Oct 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.400-alt1
- db updates (Jubilee)

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.399-alt1
- db updates

* Thu Jul 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.398-alt1
- db updates

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.397-alt1
- db updates

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.396-alt1
- db updates

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.395-alt1
- db cleanup

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.394-alt1
- db updates

* Mon May 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.393-alt1
- db updates

* Thu May 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.392-alt1
- db updates

* Sat May 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.391-alt1
- db updates
