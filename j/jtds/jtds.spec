BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          jtds
Version:       1.2.6
Release:       alt1_1jpp7
Summary:       SQL Server and Sybase JDBC driver
Group:         Development/Java
License:       MIT and LGPLv2+
URL:           http://jtds.sourceforge.net/
# wget http://sourceforge.net/projects/jtds/files/jtds/1.2.6/jtds-1.2.6-src.zip
# cleanup
# rm -rf lib doc html *.bat
# Files without proper copyright notices and unused
# rm -vrf src/SSO
# rm -vrf src/XA
# rm -vf src/test/net/sourceforge/jtds/test/{AsTest.java,CSUnitTest.java,DatabaseTestCase.java,JDBC3Test.java,NtlmAuthTest.java,SAfeTest.java,SanityTest.java,Tds5Test.java,TestBase.java,TimestampTest.java,UpdateTest.java}
# rm -vf src/tools/net/sourceforge/jtds/tools/{PacketLogger.java,SQLProxy.java,SqlForwarder.java}
# find . -name '*.jar' -o -name '*.class' -o -name '*.bat' -delete
# tar czf jtds-1.2.6-clean-src.tar.gz jtds-1.2.6
Source0:       %{name}-%{version}-clean-src.tar.gz
# remove org.codehaus.mojo truezip-maven-plugin 1.0-beta-2
Patch0:        %{name}-1.2.5-pom.patch
# fix libraries path
# disable test unavailable deps
# fix javac/javadoc source/target/encoding parameters
# remove classpath from manifest
Patch1:        %{name}-%{version}-build.patch

Patch2:        %{name}-%{version}-update-fsf-address.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: jcifs
BuildRequires: jdbc-stdext

Requires:      jcifs

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
TDS is an open source 100%% pure Java (type 4) JDBC 3.0 driver 
for Microsoft SQL Server (6.5, 7, 2000,2005, and 2008) and
Sybase (10, 11, 12, 15). jTDS is based on FreeTDS and is currently the
fastest production-ready JDBC  driver for SQL Server and Sybase.
jTDS is 100%% JDBC 3.0 compatible, supporting forward-only and
scrollable/updateable ResultSets, concurrent (completely 
independent) Statements and implementing all the DatabaseMetaData and 
ResultSetMetaData methods. 

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

for d in CHANGELOG LICENSE README* ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

%patch0 -p0
%patch1 -p0
%patch2 -p1

# fix non ASCII chars
for s in src/main/net/sourceforge/jtds/jdbc/JtdsDatabaseMetaData.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%build

%ant dist

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/doc/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc CHANGELOG LICENSE README*

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt1_1jpp7
- new version

