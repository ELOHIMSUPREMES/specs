Name: libcontrol++
Version: 0.12.0
Release: alt1

Summary: control++ common classes and functions library
License: GPLv3
Group: Development/Other
Url: https://www.altlinux.org/Control++

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=libcontrolplusplus.git
Source: %name-%version.tar

BuildRequires: gcc-c++

%define libcontrol++_desc \
libcontrol++ provides common classes and functions,\
that can be used in other app\
(such as ini-parser or file-operations).

%description
control++ is a simple system configuration tool
that allows administrator to change system ulimits,
set permission modes and, in perspective,
perform other administrative operations.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# libcontrol++-devel

%package -n libcontrol++-devel
Summary: libcontrol++ headers
Group: Development/Other
Requires: libcontrol++

%description -n libcontrol++-devel
Development package for libcontrol++.
%libcontrol++_desc

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup

%build
mkdir -p bin/Release
mkdir -p obj/Release
%make_build -C libcontrol++/ release

%install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir/libcontrol++
# Executables
cp libcontrol++/bin/Release/libcontrol++.so %buildroot%_libdir
# Includes
cp libcontrol++/src/*.h %buildroot%_includedir/libcontrol++

%files
%_libdir/*.so

%files -n libcontrol++-devel
%_includedir/libcontrol++/

%changelog
* Mon Sep 10 2018 Alexey Appolonov <alexey@altlinux.org> 0.12.0-alt1
- New section for the filestat-related functions;
- Function for opening the dir and performing the operation inside of it;
- Ability to call the function for the dir or all the files of the dir;
- Ability to add new assgn to the conf DOM and to the conf file;
- Ability to rewrite conf file completely according to DOM;
- Functions for checking/cutting an extension of a filename;
- Function for forming vector of names of all the sectors of the conf file;
- Function for determining special reference dirs;
- Function for converting string to lowercase;
- Lots of small fixes and improvements.

* Fri Jul 27 2018 Alexey Appolonov <alexey@altlinux.org> 0.11.0-alt1
- Introducing refs and const modifier wherever possible;
- Functions for trimming the string;
- Function to access the last element of the conf DOM;
- Attempt to write an empty string to a file not considered as an error;
- Explicit templates instances and unused typedefs was removed.

* Sat Jun 09 2018 Alexey Appolonov <alexey@altlinux.org> 0.10.0-alt1
- Revised PrintOnEntireLine function.

* Sat Jun 09 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.1-alt2
- libcontrol++ is a separate package now.

* Sat Jun 02 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.1-alt1
- Memory leakage fix.

* Mon May 21 2018 Alexey Appolonov <alexey@altlinux.org> 0.9.0-alt1
- New libcontrol++ features.

* Fri Mar 16 2018 Alexey Appolonov <alexey@altlinux.org> 0.8.0-alt1
- New libcontrol++ features.

* Mon Feb 26 2018 Alexey Appolonov <alexey@altlinux.org> 0.7.0-alt1
- New libcontrol++ features.

* Wed Feb 14 2018 Alexey Appolonov <alexey@altlinux.org> 0.6.0-alt1
- Common classes and functions that can be used in other projects
  compiled as libcontrol++.so
  therefore libcontrol++ and libcontrol++-devel subpackages.

* Fri Jan 26 2018 Alexey Appolonov <alexey@altlinux.org> 0.5.1-alt1
- Code restyling.
- Minor changes in units handling.

* Mon Dec 11 2017 Alexey Appolonov <alexey@altlinux.org> 0.5.0-alt1
- New unit, that runs script stated in configuration file.

* Mon Dec 4 2017 Alexey Appolonov <alexey@altlinux.org> 0.4.2-alt1
- Handling of values in quotes in configuration files.
- Verbose output with -v param when setting mode.

* Thu Nov 30 2017 Alexey Appolonov <alexey@altlinux.org> 0.4.1-alt1
- Comment lines passing in configuration files.

* Thu Nov 30 2017 Alexey Appolonov <alexey@altlinux.org> 0.4.0-alt1
- Ability to set permission modes.

* Mon Nov 27 2017 Alexey Appolonov <alexey@altlinux.org> 0.3.0-alt1
- Restructure for better extensibility.

* Mon Nov 27 2017 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Support of INI file format for the configuration file. 

* Fri Nov 17 2017 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial ALT Linux release.
