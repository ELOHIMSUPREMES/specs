Name: ansible
Summary: SSH-based configuration management, deployment, and task execution system
Version: 1.6.8
Release: alt1

Group: System/Libraries
License: GPLv3
Source0: http://ansibleworks.com/releases/%name-%version.tar
Patch0:%name-%version-alt.patch
Url: http://ansibleworks.com

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires: python-module-setuptools

%description
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

%prep
%setup
%patch0 -p1

%build
%python_build

%install
%python_install
mkdir -p %buildroot%_sysconfdir/%name/
cp examples/hosts %buildroot%_sysconfdir/%name/
cp examples/ansible.cfg %buildroot%_sysconfdir/%name/
mkdir -p %buildroot/%_man1dir
cp -v docs/man/man1/*.1 %buildroot/%_man1dir/
mkdir -p %buildroot/%_datadir/%name
cp -va library/* %buildroot/%_datadir/%name/

%files
%_bindir/%{name}*
%config(noreplace) %_sysconfdir/%name
%_datadir/%name
%_man1dir/%{name}*
%python_sitelibdir/%{name}*
%doc examples/playbooks examples/scripts
%doc README.md CONTRIBUTING.md CHANGELOG.md RELEASES.txt CODING_GUIDELINES.md

%changelog
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
