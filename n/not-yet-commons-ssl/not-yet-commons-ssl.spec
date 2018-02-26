Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           not-yet-commons-ssl
Version:        0.3.11
Release:        alt1_8jpp7
Summary:        Library to make SSL and Java Easier

Group:          Development/Java
License:        ASL 2.0
URL:            http://juliusdavies.ca/commons-ssl
Source0:        http://juliusdavies.ca/commons-ssl/not-yet-commons-ssl-0.3.11.zip
Source1:        %{name}-MANIFEST.MF
Source2:		%{name}-%{version}.pom
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  log4j
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  bouncycastle
BuildRequires:  ant-junit
BuildRequires:  zip
Requires:       log4j
Requires:       jakarta-commons-httpclient
Requires:       jpackage-utils
Source44: import.info

%description
Commons-SSL lets you control the SSL options you need in an 
natural way for each SSLSocketFactory, and those options won't 
bleed into the rest of your system.

%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
rm -fr javadocs/

%build
export CLASSPATH=$(build-classpath log4j commons-httpclient bcprov)
ant -Dbuild.sysclasspath=first jar test javadoc

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/commons-ssl.jar META-INF/MANIFEST.MF

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/commons-ssl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/javadocs/*  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -dm 755 %{buildroot}/%{_mavenpomdir}
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/*
%doc LICENSE.txt NOTICE.txt README.txt
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:0.3.11-alt1_8jpp7
- fc update

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.3.11-alt1_2jpp6
- new version

