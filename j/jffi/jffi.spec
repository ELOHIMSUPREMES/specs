Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++ texinfo unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global cluster jnr
%global sover 1.2

Name:           jffi
Version:        1.2.9
Release:        alt2_8jpp8
Summary:        Java Foreign Function Interface

License:        LGPLv3+ or ASL 2.0
URL:            http://github.com/jnr/jffi
Source0:        https://github.com/%{cluster}/%{name}/archive/%{version}.zip
Source1:        MANIFEST.MF
Source2:        NATIVE-MANIFEST.MF
Source3:        p2.inf
Patch0:         jffi-fix-dependencies-in-build-xml.patch
Patch1:         jffi-add-built-jar-to-test-classpath.patch
Patch2:         jffi-fix-compilation-flags.patch

BuildRequires:  maven-local
BuildRequires:  libffi-devel
BuildRequires:  ant
BuildRequires:  ant-junit
Source44: import.info

%description
An optimized Java interface to libffi.

%package native
Group: System/Libraries
Summary:        %{name} JAR with native bits

%description native
This package contains %{name} JAR with native bits.

%package javadoc
Group: System/Libraries
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
cp %{SOURCE1} .
cp %{SOURCE2} .
sed -i -e's/@VERSION/%{version}/g' MANIFEST.MF
sed -i -e's/@VERSION/%{version}/g' NATIVE-MANIFEST.MF
%patch0
%patch1
%patch2

# ppc{,64} fix
# https://bugzilla.redhat.com/show_bug.cgi?id=561448#c9
sed -i.cpu -e '/m\$(MODEL)/d' jni/GNUmakefile libtest/GNUmakefile

# remove uneccessary directories
rm -rf archive/* jni/libffi/ jni/win32/ lib/CopyLibs/ lib/junit*

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

build-jar-repository -s -p lib/ junit

%mvn_package 'com.github.jnr:jffi::native:' native
%mvn_file ':{*}' %{name}/@1 @1

%build
# ant will produce JAR with native bits
ant jar build-native -Duse.system.libffi=1

# maven will look for JAR with native bits in archive/
cp -p dist/jffi-*-Linux.jar archive/

%mvn_build

%install
%mvn_install

mkdir -p META-INF/
cp %{SOURCE3} META-INF/
jar umf MANIFEST.MF %{buildroot}%{_jnidir}/%{name}/%{name}.jar META-INF/p2.inf

# install *.so
install -dm 755 %{buildroot}%{_libdir}/%{name}
cp -rp target/jni/* %{buildroot}%{_libdir}/%{name}/
# create version-less symlink for .so file
sofile=`find %{buildroot}%{_libdir}/%{name} -name lib%{name}-%{sover}.so`
chmod +x ${sofile}
ln -sr ${sofile} `dirname ${sofile}`/lib%{name}.so

jar umf NATIVE-MANIFEST.MF %{buildroot}%{_jnidir}/%{name}/%{name}-native.jar

%check
# skip tests on s390 until https://bugzilla.redhat.com/show_bug.cgi?id=1084914 is resolved
%ifnarch s390
# don't fail on unused parameters... (TODO: send patch upstream)
sed -i 's|-Werror||' libtest/GNUmakefile
ant -Duse.system.libffi=1 test
%endif

%files -f .mfiles
%doc COPYING.GPL COPYING.LESSER LICENSE

%files native -f .mfiles-native
%{_libdir}/%{name}
%doc COPYING.GPL COPYING.LESSER LICENSE

%files javadoc -f .mfiles-javadoc
%doc COPYING.GPL COPYING.LESSER LICENSE

%changelog
* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt2_8jpp8
- %%_jnidir set to /usr/lib/java

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1_8jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt2_3jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt2_1jpp7
- added symlink in javadir

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt1_1jpp7
- new version

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt3_1jpp7
- fixed build

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt2_1jpp7
- gcc47 build

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_1jpp7
- new version

