Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name codec
%global short_name commons-%{base_name}

Name:          apache-%{short_name}
Version:       1.8
Release:       alt1_5jpp7
Summary:       Implementations of common encoders and decoders
Group:         Development/Java
License:       ASL 2.0
URL:           http://commons.apache.org/%{base_name}/

Source0:       http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# Data in DoubleMetaphoneTest.java originally has an inadmissible license.
# The author gives MIT in e-mail communication.
Source1:       aspell-mail.txt


BuildArch:     noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
Requires:      jpackage-utils

# It looks like there are packages in F-18 that BR/R the short name
Provides:      %{short_name} = %{version}-%{release}
Obsoletes:     %{short_name} < %{version}-%{release}
# Provide and obsolete jakarta-commons-codec to support installing this
# package on RHEL 6, which still uses the old jakarta-commons-* package
# naming scheme.
Provides:      jakarta-%{short_name} = %{version}-%{release}
Obsoletes:     jakarta-%{short_name} < %{version}-%{release}
Source44: import.info

%description
Commons Codec is an attempt to provide definitive implementations of
commonly used encoders and decoders. Examples include Base64, Hex,
Phonetic and URLs.

%package javadoc
Summary:       API documentation for %{name}
Group:         Development/Java
Requires:      jpackage-utils
Provides:      jakarta-%{short_name}-javadoc = %{version}-%{release}
Obsoletes:     jakarta-%{short_name}-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} aspell-mail.txt
sed -i 's/\r//' RELEASE-NOTES*.txt LICENSE.txt NOTICE.txt

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{short_name}.pom
%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar -a "%{short_name}:%{short_name}"
# jakarta compat
ln -s %{short_name}.jar %buildroot%_javadir/jakarta-%{short_name}.jar
#ln -s %{short_name}.jar %buildroot%_javadir/apache-%{short_name}.jar


%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES* aspell-mail.txt
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*
%{_javadir}/*

%files javadoc
%doc LICENSE.txt NOTICE.txt aspell-mail.txt
%{_javadocdir}/%{name}

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_5jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_5jpp7
- new version

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp7
- added OSGi manifest

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp7
- new version

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_5jpp6
- fixed repolib

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_5jpp6
- fixed repolib

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_5jpp6
- new version

