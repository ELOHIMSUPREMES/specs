Name: ansible
Summary: SSH-based configuration management, deployment, and task execution system
Version: 1.9.4
Release: alt1

Group: System/Libraries
License: GPLv3
Source0: %name-%version.tar
Source1: %name-modules-core-%version.tar
Source2: %name-modules-extras-%version.tar

Patch0:%name-%version-alt.patch
Patch1: %name-modules-core-%version-alt.patch

Url: http://www.ansible.com

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires: python-module-setuptools

# Skip findreq on all modules:
%add_findreq_skiplist %python_sitelibdir/%name/modules/*

%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%prep
%setup
%patch0 -p1
tar -xvf %SOURCE1               # creates ./library/...
tar -xvf %SOURCE2
pushd library
%patch1 -p1
popd

%build
%python_build

%install
%python_install
mkdir -p %buildroot%_sysconfdir/%name/
cp examples/ansible.cfg %buildroot%_sysconfdir/%name/
touch %buildroot%_sysconfdir/%name/hosts
mkdir -p %buildroot/%_man1dir
cp -v docs/man/man1/*.1 %buildroot/%_man1dir/
rm -f library/{VERSION,README.md,COPYING,CONTRIBUTING.md}
cp -va library/* %buildroot%python_sitelibdir/%name/modules

%files
%_bindir/%{name}*
%config(noreplace) %_sysconfdir/%name
%_man1dir/%{name}*
%python_sitelibdir/%{name}*
%doc examples/playbooks examples/scripts examples/hosts
%doc README.md CONTRIBUTING.md CHANGELOG.md RELEASES.txt CODING_GUIDELINES.md ISSUE_TEMPLATE.md

%changelog
* Tue Oct 20 2015 Terechkov Evgenii <evg@altlinux.org> 1.9.4-alt1
- 1.9.4

* Sat Jun 27 2015 Terechkov Evgenii <evg@altlinux.org> 1.9.2-alt1
- 1.9.2 (ALT#30995)

* Sat Feb 28 2015 Terechkov Evgenii <evg@altlinux.org> 1.8.4-alt1
- 1.8.4

* Fri Jan  2 2015 Terechkov Evgenii <evg@altlinux.org> 1.8.2-alt2
- Fix modules location (ALT#30619)
- Drop default hosts file (see examples/hosts, ALT#30620)

* Sun Dec  7 2014 Terechkov Evgenii <evg@altlinux.org> 1.8.2-alt1
- 1.8.2

* Sat Nov 29 2014 Terechkov Evgenii <evg@altlinux.org> 1.8.1-alt1
- 1.8.1

* Tue Oct 21 2014 Terechkov Evgenii <evg@altlinux.org> 1.7.2-alt1
- 1.7.2

* Thu Aug 21 2014 Terechkov Evgenii <evg@altlinux.org> 1.7.1-alt1
- 1.7.1

* Sat Aug  9 2014 Terechkov Evgenii <evg@altlinux.org> 1.7.0-alt2
- Oops, apt-rpm module renamed to apt_rpm (update your playbooks!)

* Fri Aug  8 2014 Terechkov Evgenii <evg@altlinux.org> 1.7.0-alt1
- 1.7.0

* Sat Jul 26 2014 Terechkov Evgenii <evg@altlinux.org> 1.6.8-alt1
- 1.6.8
- CVE-2014-4966 and CVE-2014-4967 fixed in v1.6.7


* Sun Jun  1 2014 Terechkov Evgenii <evg@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri May 23 2014 Terechkov Evgenii <evg@altlinux.org> 1.6.1-alt2
- Relax suds module requirement

* Wed May 21 2014 Terechkov Evgenii <evg@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Apr 22 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.5-alt1
- 1.5.5

* Tue Apr  8 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.4-alt2
- Fix for apt-rpm module (changed run_command behavior)

* Wed Apr  2 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.4-alt1
- 1.5.4

* Tue Apr  1 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.3-alt1
- 1.5.3

* Fri Mar 14 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.0-alt2
- Revert wrongly patched files to tag v1.5.0

* Wed Mar  5 2014 Terechkov Evgenii <evg@altlinux.org> 1.5.0-alt1
- 1.5.0 (ALT #29865)

* Sun Jan 19 2014 Terechkov Evgenii <evg@altlinux.org> 1.4.4-alt2
- apt-rpm: Properly detect rpm packages installation/upgrade.

* Sun Jan 12 2014 Terechkov Evgenii <evg@altlinux.org> 1.4.4-alt1
- 1.4.4

* Mon Dec 30 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.3-alt3
- Fix in apt-rpm module (upgrade installed packages as documented)

* Sun Dec 29 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.3-alt2
- apt-rpm module added

* Sun Dec 29 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.3-alt1
- 1.4.3

* Sun Dec  1 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.1-alt1
- 1.4.1

* Tue Nov 26 2013 Terechkov Evgenii <evg@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Nov 11 2013 Terechkov Evgenii <evg@altlinux.org> 1.3.4-alt1
- 1.3.4

* Tue Oct  8 2013 Terechkov Evgenii <evg@altlinux.org> 1.3.3-alt1
- 1.3.3

* Sun Sep 29 2013 Terechkov Evgenii <evg@altlinux.org> 1.3.2-alt1
- 1.3.2
