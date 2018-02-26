Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          xapool
Version:       1.5.0
Release:       alt4_2jpp7
Summary:       Open source XA JDBC Pool
Group:         Development/Java
License:       LGPLv2+
URL:           http://xapool.ow2.org/
# wget http://download.forge.objectweb.org/xapool/xapool-1.5.0-src.tgz
# tar -xf xapool-1.5.0-src.tgz
# find xapool-1.5.0-src -name "*.jar" -delete
# find xapool-1.5.0-src -name "*.class" -delete
# find xapool-1.5.0-src -name "*.java~" -delete
# rm -rf $(find xapool-1.5.0-src -name "CVS")
# tar czf xapool-1.5.0-src-clean.tar.gz xapool-1.5.0-src
Source0:       %{name}-%{version}-src-clean.tar.gz
Source1:       http://repo1.maven.org/maven2/com/experlog/%{name}/%{version}/%{name}-%{version}.pom
# disable p6spy howl-logger oracle classes12 support
Patch0:        %{name}-%{version}-build.patch
Patch1:        %{name}-%{version}-jdk7.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: apache-commons-logging
BuildRequires: geronimo-jta

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
XAPool is a software component which allows to:

 - Store objects with a Generic Pool
 - Export a DataSource (javax.sql.DataSource)
 - Export a XADataSource (javax.sql.XADataSource)

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
find . -name "*.jar" -delete
find . -name "*.class" -delete
find . -name "*.java~" -delete

rm -rf $(find . -name "CVS")

%patch0 -p0
%patch1 -p1
sed -i "s|Class-Path: idb.jar classes12.jar jta-spec1_0_1.jar log4j.jar commons-logging.jar p6psy.jar||" archive/xapool.mf

ln -sf $(build-classpath commons-logging) externals/
ln -sf $(build-classpath geronimo-jta) externals/

rm -r src/org/enhydra/jdbc/instantdb \
  src/org/enhydra/jdbc/oracle

%build

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  dist

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 output/dist/lib/%{name}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr output/dist/jdoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc README.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt4_2jpp7
- fc update

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt3_3jpp6
- jpp 6 release

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt3_2jpp5
- new jpp release

* Thu Feb 26 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt3_1jpp5
- fixed build

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt2_1jpp5
- fixed build with java 5

* Thu Nov 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

