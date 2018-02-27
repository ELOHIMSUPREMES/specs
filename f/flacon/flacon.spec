Name: flacon
Version: 0.9.3
Release: alt1

Summary: Audio File Encoder
Summary(ru_RU.UTF-8): Конвертер аудиофайлов
Summary(uk_UA.UTF-8): Кодувальник аудіофайлів
License: LGPLv2.1
Group: Sound

Url: http://%name.github.io/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: %name-%version.tar.gz

Requires: shntool

BuildRequires: cmake gcc-c++ libuchardet-devel phonon-devel

%description
Extracts audio tracks from audio CD image to separate tracks.

%description -l ru_RU.UTF-8
Извлекает аудио треки из CD образа WAV, FLAC, APE в отдельные файлы.

%description -l uk_UA.UTF-8
Витягує доріжки з образу аудіо-CD.

%prep
%setup

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_CXX_FLAGS:STRING='%optflags'

popd

%make_build -C %_target_platform	
	
%install
%makeinstall_std -C %_target_platform

%files
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_liconsdir/%name.png
%_niconsdir/%name.png
%_datadir/%name
%_man1dir/%name.1.gz

%changelog
* Thu Jan 16 2014 Nazarov Denis <nenderus@altlinux.org> 0.9.3-alt1
- Version 0.9.3

* Sun Oct 27 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.2-alt0.M70P.1
- Build for branch p7

* Sun Oct 27 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.2-alt0.M70T.1
- Build for branch t7

* Sun Oct 27 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.2-alt1
- Version 0.9.2

* Thu Oct 17 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt0.M60P.1
- Build for branch p6

* Wed Oct 16 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt0.M60T.1
- Build for branch t6

* Wed Oct 16 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt0.M70P.1
- Build for branch p7

* Tue Oct 15 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt0.M70T.1
- Build for branch t7

* Tue Oct 15 2013 Nazarov Denis <nenderus@altlinux.org> 0.9.1-alt1
- Version 0.9.1 (ALT #29478)

* Sat May 25 2013 Nazarov Denis <nenderus@altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Thu Aug 23 2012 Nazarov Denis <nenderus@altlinux.org> 0.7.2-alt0.M60P.1
- Build for branch p6

* Mon Aug 20 2012 Nazarov Denis <nenderus@altlinux.org> 0.7.2-alt0.M60T.1
- Build for branch t6

* Mon Aug 20 2012 Nazarov Denis <nenderus@altlinux.org> 0.7.2-alt1
- Version 0.7.2

* Wed Aug 08 2012 Nazarov Denis <nenderus@altlinux.org> 0.7.1-alt0.M60T.1
- Build for branch t6

* Wed Aug 08 2012 Nazarov Denis <nenderus@altlinux.org> 0.7.1-alt1
- Version 0.7.1

* Mon Feb 20 2012 Nazarov Denis <nenderus@altlinux.org> 0.6.1-alt0.M60T.1
- Build for branch t6

* Mon Feb 20 2012 Nazarov Denis <nenderus@altlinux.org> 0.6.1-alt1
- Version 0.6.1

* Sat Dec 10 2011 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt0.M60T.1
- Build for branch t6

* Sat Dec 10 2011 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt1
- Version 0.6.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.7-alt1.1
- Rebuild with Python-2.7

* Fri May 27 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.7-alt0.M60T.1
- Build for branch t6

* Mon May 09 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.7-alt1
- Version 0.5.7

* Sun Feb 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.6-alt0.M41.1
- Build for branch 4.1

* Sun Feb 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.6-alt0.M51.1
- Build for branch 5.1

* Sun Feb 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.6-alt1
- Version 0.5.6

* Fri Feb 11 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.5-alt0.M51.1
- Build for branch 5.1

* Fri Feb 11 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.5-alt1
- Version 0.5.5

* Sat Jan 29 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.4-alt0.M51.1
- Build for branch 5.1

* Sat Jan 29 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.4-alt1
- Version 0.5.4

* Fri Nov 26 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.3-alt0.M51.1
- Build for branch 5.1

* Fri Nov 26 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.3-alt1
- Version 0.5.3

* Sun Oct 31 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.2-alt0.M51.1
- Build for branch 5.1

* Fri Oct 29 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.2-alt1
- Version 0.5.2

* Wed Oct 20 2010 Motsyo Gennadi <drool@altlinux.ru> 0.5.1-alt0.M41.1
- build for M41

* Tue Oct 19 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.1-alt0.M51.1
- Build for branch 5.1

* Mon Oct 18 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.1-alt1
- Version 0.5.1

* Mon Oct 04 2010 Nazarov Denis <nenderus@altlinux.org> 0.5-alt0.M51.1
- Build for branch 5.1

* Mon Oct 04 2010 Nazarov Denis <nenderus@altlinux.org> 0.5-alt1
- Version 0.5

* Thu Aug 19 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.7-alt0.M51.1
- Build for branch 5.1

* Thu Aug 19 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.7-alt1
- Version 0.4.7

* Sun Aug 08 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.5-alt0.M51.1
- Build for branch 5.1

* Sun Aug 08 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.5-alt1
- Version 0.4.5

* Sun Aug 01 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.4-alt0.M51.1
- Build for branch 5.1

* Sun Aug 01 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.4-alt1
- Version 0.4.4

* Sat Jul 24 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.3-alt0.M51.1
- Build for branch 5.1

* Sat Jul 24 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.3-alt1
- Version 0.4.3

* Sun Jun 13 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.2-alt0.M51.1
- Build for branch 5.1

* Sun Jun 13 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.2-alt1
- Version 0.4.2

* Mon May 31 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt0.M51.1
- Build for branch 5.1

* Mon May 31 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt1
- Version 0.4.1

* Fri May 28 2010 Nazarov Denis <nenderus@altlinux.org> 0.4-alt0.M51.1
- Build for branch 5.1

* Fri May 28 2010 Nazarov Denis <nenderus@altlinux.org> 0.4-alt1
- Version 0.4

* Wed May 12 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1.M51.3
- Build for branch 5.1

* Fri Apr 30 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt2.2
- Fix desktop-file

* Tue Apr 27 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1.M51.2
- Build for branch 5.1

* Tue Apr 27 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt2.1
- Cleanup spec-file

* Mon Apr 26 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1.M51.1
- First build for branch 5.1

* Mon Apr 12 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt2
- Fix requires, buildarch and icons

* Fri Apr 9 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1
- First build for ALT Linux 5.0 (p5)
