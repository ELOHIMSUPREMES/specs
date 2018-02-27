Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: sac
Version: 1.3
Release: alt3_13jpp7
Summary: Java standard interface for CSS parser
License: W3C
Group: System/Libraries
Source0: http://www.w3.org/2002/06/%{name}java-%{version}.zip
Source1: %{name}-build.xml
Source2: %{name}-MANIFEST.MF
Source3: http://mirrors.ibiblio.org/pub/mirrors/maven2/org/w3c/css/sac/1.3/sac-1.3.pom
URL: http://www.w3.org/Style/CSS/SAC/
BuildRequires: ant jpackage-utils zip
Requires: jpackage-utils
BuildArch: noarch
Source44: import.info

%description
SAC is a standard interface for CSS parsers, intended to work with CSS1, CSS2,
CSS3 and other CSS derived languages.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
install -m 644 %{SOURCE1} build.xml
find . -name "*.jar" -exec rm -f {} \;

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar javadoc

%install

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/sac.jar META-INF/MANIFEST.MF

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./build/lib/sac.jar $RPM_BUILD_ROOT%{_javadir}/sac.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_to_maven_depmap org.w3c.css sac %{version} JPP sac

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE3} \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%files
%doc COPYRIGHT.html
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

%changelog
* Fri Apr 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_13jpp7
- added osgi provides

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_13jpp7
- new release

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_7jpp6
- updated OSGi manifest

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_7jpp6
- added osgi manifest

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_4jpp5
- first build

