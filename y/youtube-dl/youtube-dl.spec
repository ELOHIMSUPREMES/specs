%define py_name youtube_dl

Name: youtube-dl
Version: 2016.04.13
Release: alt1

Summary: Download videos from YouTube
License: Public domain
Group: Networking/File transfer
Url: http://youtube-dl.org

Source0: %name-%version.tar

BuildArch: noarch

Requires: python-module-youtube_dl = %EVR

# Automatically added by buildreq on Fri Apr 08 2016
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python3 python3-base
BuildRequires: python-module-setuptools python3-dev python3-module-setuptools
BuildRequires(pre): rpm-build-python3

%description
Youtube-dl is a small command-line program to download videos
from YouTube.com.

%package -n python-module-%py_name
Group: Development/Python
Summary: Python module for youtube-dl
Conflicts: youtube-dl < 2016.04.06-alt1

%description -n python-module-%py_name
Youtube-dl is a small command-line program to download videos
from YouTube.com.

This package contains Python module.

%package -n python3-module-%py_name
Group: Development/Python
Summary: Python 3 module for youtube-dl
%py3_provides %py_name

%description -n python3-module-%py_name
Youtube-dl is a small command-line program to download videos
from YouTube.com.

This package contains Python 3 module.

%prep
%setup -c
for py in py2 py3; do
	cp -a %name-%version $py
done

%build
cd py2
	%python3_build
cd -

cd py3
	%python_build
cd -

%install
cd py2
	%python3_install
cd -

cd py3
	%python_install
cd -

%files
%_bindir/youtube-dl
%_man1dir/youtube-dl.1.*

%files -n python-module-%py_name
%python_sitelibdir/%py_name
%python_sitelibdir/%py_name-*.egg-info

%files -n python3-module-%py_name
%python3_sitelibdir/%py_name
%python3_sitelibdir/%py_name-*.egg-info

%changelog
* Fri Apr 15 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2016.04.13-alt1
- Updated to 2016.04.13.
- python3-module-youtube_dl: added P: python3(youtube_dl) (ALT#31948).

* Fri Apr 08 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2016.04.06-alt1
- Updated to 2016.04.06.
- Split package into youtube-dl and python module.
- Packaged python3 module (ALT#31948).

* Wed Mar 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2016.03.27-alt1
- Updated to 2016.03.27.

* Fri Mar 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2016.03.01-alt1
- Updated to 2016.03.01.

* Mon Feb 15 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2016.02.13-alt1
- Updated to 2016.02.13.

* Mon Feb 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 2016.01.31-alt1
- Updated to 2016.01.31.

* Fri Dec 11 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.12.10-alt1
- Updated to 2015.12.10.

* Fri Nov 06 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.11.02-alt1
- Updated to 2015.11.02.

* Wed Oct 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.10.13-alt1
- Updated to 2015.10.13.

* Thu Aug 27 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.08.23-alt1
- Updated to 2015.08.23.

* Sun Aug 02 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.07.28-alt1
- Updated to 2015.07.28.

* Tue Jul 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.07.07-alt1
- Updated to 2015.07.07.

* Fri Jun 26 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.06.25-alt1
- Updated to 2015.06.25.

* Thu May 21 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.05.20-alt1
- Updated to 2015.05.20.

* Wed May 06 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.05.04-alt1
- Updated to 2015.05.04.

* Tue Mar 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.03.09-alt1
- Updated to 2015.03.09.

* Wed Feb 11 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.02.10.5-alt1
- Updated to 2015.02.10.5.

* Mon Feb 02 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.02.02-alt1
- Updated to 2015.02.02.

* Wed Jan 28 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2015.01.25-alt1
- Updated to 2015.01.25.

* Thu Jul 24 2014 Mykola Grechukh <gns@altlinux.ru> 2014.07.24-alt2
- 2014.07.24

* Mon Apr 08 2013 Mykola Grechukh <gns@altlinux.ru> 2013.04.03-alt2
- build from source tree

* Mon Apr 08 2013 Mykola Grechukh <gns@altlinux.ru> 2013.04.03-alt1
- 2011.08.04 -> 2013.04.03

* Fri Aug 05 2011 Mykola Grechukh <gns@altlinux.ru> 2011.08.04-alt1
- 2010.12.09 -> 2011.08.04

* Fri Dec 24 2010 Mykola Grechukh <gns@altlinux.ru> 2010.12.09-alt1
- 2010.08.04 -> 2010.12.09

* Fri Aug 27 2010 Mykola Grechukh <gns@altlinux.ru> 2010.08.04-alt1
- 2010.03.13 -> 2010.08.04

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 2010.03.13-alt1
- 2010.01.19 -> 2010.03.13

* Sat Jan 23 2010 Igor Zubkov <icesik@altlinux.org> 2010.01.19-alt1
- 2010.01.06 -> 2010.01.19

* Tue Jan 12 2010 Igor Zubkov <icesik@altlinux.org> 2010.01.06-alt1
- 2009.12.26 -> 2010.01.06

* Tue Dec 29 2009 Igor Zubkov <icesik@altlinux.org> 2009.12.26-alt1
- 2009.09.13 -> 2009.12.26

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.09.13-alt1.1
- Rebuilt with python 2.6

* Sat Sep 19 2009 Igor Zubkov <icesik@altlinux.org> 2009.09.13-alt1
- 2009.09.08 -> 2009.09.13

* Sun Sep 13 2009 Igor Zubkov <icesik@altlinux.org> 2009.09.08-alt1
- 2009.08.08 -> 2009.09.08

* Wed Aug 26 2009 Igor Zubkov <icesik@altlinux.org> 2009.08.08-alt1
- 2009.06.29 -> 2009.08.08

* Fri Jul 31 2009 Igor Zubkov <icesik@altlinux.org> 2009.06.29-alt1
- 2009.03.03 -> 2009.06.29

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 2009.03.03-alt1
- 2008.11.01 -> 2009.03.03

* Sun Nov 16 2008 Igor Zubkov <icesik@altlinux.org> 2008.11.01-alt1
- 2008.07.26 -> 2008.11.01

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 2008.07.26-alt1
- youtube-dl from  2008.07.26
- move metacafe-dl and pornotube-dl to separate packages
- update License -> Public domain

* Thu Jul 10 2008 Igor Zubkov <icesik@altlinux.org> 2008.06.08-alt1
- youtube-dl from 2008.06.08
- metacafe-dl from 2008.06.07
- pornotube-dl from 2008.06.03

* Sun Feb 03 2008 Grigory Batalov <bga@altlinux.ru> 2008.01.28-alt1.1
- Rebuilt with python-2.5.

* Tue Jan 29 2008 Pavlov Konstantin <thresh@altlinux.ru> 2008.01.28-alt1
- youtube-dl from 2008.01.24.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.10.12-alt1
- youtube-dl from 2007.10.12.
- metacafe-dl from 2007.10.09.
- pornotube-dl from 2007.10.09.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.09.13-alt1
- youtube-dl from 2007.08.24.
- metacafe-dl from 2007.09.13.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.06.22-alt1
- youtube-dl from 2007.06.22.
- pornotube-dl from 2007.05.22.

* Fri Apr 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.03.27-alt1
- 2007.03.27 version.

* Thu Mar 01 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.02.18-alt2
- Fix wrong symlink.

* Tue Feb 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.02.18-alt1
- Initial build for ALT Linux.

