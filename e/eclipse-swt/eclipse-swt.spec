Epoch: 1
Name: eclipse-swt
Version: 4.7.3
Summary: SWT Library for GTK+
License: EPL
Url: http://www.eclipse.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: eclipse-swt = 1:4.7.3a-4.fc28
Provides: mvn(org.eclipse.swt:org.eclipse.swt) = 3.106.3.v20180409.1128
Provides: mvn(org.eclipse.swt:swt) = 3.106.3.v20180409.1128
Provides: osgi(org.eclipse.swt) = 3.106.3
Requires: libgtk+2
Requires: libgtk+3
Requires: java
Requires: libwebkitgtk2
Requires: libwebkitgtk3

Group: Development/Java
Release: alt0.1jpp

Source1: swt.i586.jar
Source2: swt.x86_64.jar
Source3: swt.aarch64.jar
Source4: eclipse-swt.xml.i586
Source5: eclipse-swt.xml.x86_64
Source6: eclipse-swt.xml.aarch64
ExclusiveArch: %ix86 x86_64 aarch64

%description
SWT Library for GTK+.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/maven-metadata
mkdir -p $RPM_BUILD_ROOT/usr/lib/java/
mkdir -p $RPM_BUILD_ROOT%_libdir/eclipse
ln -s ../../lib/java/swt.jar %buildroot%_libdir/eclipse/swt.jar

%ifarch %{ix86}
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/usr/lib/java/swt.jar
%endif
%ifarch x86_64
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/usr/lib/java/swt.jar
%endif
%ifarch aarch64
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT/usr/share/maven-metadata/eclipse-swt.xml
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/usr/lib/java/swt.jar
%endif


%files
/usr/share/maven-metadata/eclipse-swt.xml
/usr/lib/java/swt.jar
%_libdir/eclipse/swt.jar

%changelog
* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.7.3-alt0.1jpp
- updated to 4.7.3

* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt0.2jpp
- added aarch64

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt0.1jpp
- bootstrap pack of jars

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt0.2jpp
- install to %%_jnidir

* Sun Jan 24 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

