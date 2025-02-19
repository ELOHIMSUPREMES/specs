# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name:           GeoLite2-Country
Version: 20190521
Release: alt1
Summary:        Free IP geolocation %name database
License:        CC-BY-SA
Group:          Sciences/Geosciences
URL:            https://dev.maxmind.com/geoip/geoip2/geolite2/
Source0:        https://geolite.maxmind.com/download/geoip/database/%{name}_%{version}.tar.gz
BuildArch:      noarch

# recommends
# Requires:     geoipupdate

%description 
GeoLite2 country database is a free IP geolocation database comparable to, but less
accurate than, MaxMind's GeoIP2 database.

This product includes GeoLite2 data created by MaxMind,
available from http://www.maxmind.com.

%prep
%setup -q -n %{name}_%{version}


%install
install -D -p -m 0644 %{name}.mmdb %{buildroot}%{_datadir}/GeoIP/%{name}.mmdb

%files
%doc --no-dereference COPYRIGHT.txt LICENSE.txt
%dir %{_datadir}/GeoIP
# to allow updates using geoipupdate
%verify(not md5 size mtime) %{_datadir}/GeoIP/%{name}.mmdb

%changelog
* Mon May 27 2019 Cronbuild Service <cronbuild@altlinux.org> 20190521-alt1
- repocop cronbuild 20190527. At your service.

* Sun May 19 2019 Cronbuild Service <cronbuild@altlinux.org> 20190514-alt1
- repocop cronbuild 20190519. At your service.

* Sat May 11 2019 Cronbuild Service <cronbuild@altlinux.org> 20190507-alt1
- repocop cronbuild 20190511. At your service.

* Fri May 03 2019 Cronbuild Service <cronbuild@altlinux.org> 20190430-alt1
- repocop cronbuild 20190503. At your service.

* Thu Apr 25 2019 Cronbuild Service <cronbuild@altlinux.org> 20190423-alt1
- repocop cronbuild 20190425. At your service.

* Wed Apr 17 2019 Cronbuild Service <cronbuild@altlinux.org> 20190416-alt1
- repocop cronbuild 20190417. At your service.

* Tue Apr 09 2019 Cronbuild Service <cronbuild@altlinux.org> 20190409-alt1
- repocop cronbuild 20190409. At your service.

* Mon Apr 01 2019 Cronbuild Service <cronbuild@altlinux.org> 20190402-alt1
- repocop cronbuild 20190401. At your service.

* Sun Mar 24 2019 Cronbuild Service <cronbuild@altlinux.org> 20190319-alt1
- repocop cronbuild 20190324. At your service.

* Sat Mar 16 2019 Cronbuild Service <cronbuild@altlinux.org> 20190312-alt1
- repocop cronbuild 20190316. At your service.

* Fri Mar 08 2019 Cronbuild Service <cronbuild@altlinux.org> 20190305-alt1
- repocop cronbuild 20190308. At your service.

* Thu Feb 28 2019 Cronbuild Service <cronbuild@altlinux.org> 20190226-alt1
- repocop cronbuild 20190228. At your service.

* Wed Feb 20 2019 Cronbuild Service <cronbuild@altlinux.org> 20190219-alt1
- repocop cronbuild 20190220. At your service.

* Tue Feb 12 2019 Cronbuild Service <cronbuild@altlinux.org> 20190212-alt1
- repocop cronbuild 20190212. At your service.

* Mon Feb 04 2019 Cronbuild Service <cronbuild@altlinux.org> 20190129-alt1
- repocop cronbuild 20190204. At your service.

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 20180925-alt1
- new version
