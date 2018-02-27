Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%global cvs_version 2_11_0

%define __requires_exclude system.bundle

Name:          xerces-j2
Version:       2.11.0
Release:       alt1_14jpp7
Summary:       Java XML parser
Group:         Development/Java
License:       ASL 2.0
URL:           http://xerces.apache.org/xerces2-j/

Source0:       http://mirror.ox.ac.uk/sites/rsync.apache.org/xerces/j/source/Xerces-J-src.%{version}.tar.gz
Source1:       %{name}-version.sh
Source2:       %{name}-constants.sh
Source11:      %{name}-version.1
Source12:      %{name}-constants.1

# Custom javac ant task used by the build
Source3:       https://svn.apache.org/repos/asf/xerces/java/tags/Xerces-J_%{cvs_version}/tools/src/XJavac.java

# Custom doclet tags used in javadocs
Source5:       https://svn.apache.org/repos/asf/xerces/java/tags/Xerces-J_%{cvs_version}/tools/src/ExperimentalTaglet.java
Source6:       https://svn.apache.org/repos/asf/xerces/java/tags/Xerces-J_%{cvs_version}/tools/src/InternalTaglet.java

Source7:       %{name}-pom.xml

# Patch the build so that it doesn't try to use bundled xml-commons source
Patch0:        %{name}-build.patch

# Patch the manifest so that it includes OSGi stuff
Patch1:        %{name}-manifest.patch

BuildArch:     noarch

BuildRequires: jpackage-utils
BuildRequires: xalan-j2 >= 2.7.1
BuildRequires: xml-commons-apis >= 1.4.01
BuildRequires: xml-commons-resolver >= 1.2
BuildRequires: ant
BuildRequires: jaxp_parser_impl
BuildRequires: fonts-ttf-dejavu
Requires:      jpackage-utils
Requires:      xalan-j2 >= 2.7.1
Requires:      xml-commons-apis >= 1.4.01
Requires:      xml-commons-resolver >= 1.2

Provides:      jaxp_parser_impl = 1.4
Provides:      %{name}-scripts = %{version}-%{release}
Obsoletes:     %{name}-scripts < 2.11.0-6

Requires(post):  chkconfig jaxp_parser_impl
Requires(preun): chkconfig jaxp_parser_impl

# This documentation is provided by xml-commons-apis
Obsoletes:     %{name}-javadoc-apis < %{version}-%{release}

# http://mail-archives.apache.org/mod_mbox/xerces-j-dev/201008.mbox/%3COF8D7E2F83.0271A181-ON8525777F.00528302-8525777F.0054BBE0@ca.ibm.com%3E
Obsoletes:     %{name}-manual < %{version}-%{release}
Source44: import.info

%description
Welcome to the future! Xerces2 is the next generation of high performance,
fully compliant XML parsers in the Apache Xerces family. This new version of
Xerces introduces the Xerces Native Interface (XNI), a complete framework for
building parser components and configurations that is extremely modular and
easy to program.

The Apache Xerces2 parser is the reference implementation of XNI but other
parser components, configurations, and parsers can be written using the Xerces
Native Interface. For complete design and implementation documents, refer to
the XNI Manual.

Xerces2 is a fully conforming XML Schema processor. For more information,
refer to the XML Schema page.

Xerces2 also provides a complete implementation of the Document Object Model
Level 3 Core and Load/Save W3C Recommendations and provides a complete
implementation of the XML Inclusions (XInclude) W3C Recommendation. It also
provides support for OASIS XML Catalogs v1.1.

Xerces2 is able to parse documents written according to the XML 1.1
Recommendation, except that it does not yet provide an option to enable
normalization checking as described in section 2.13 of this specification. It
also handles name spaces according to the XML Namespaces 1.1 Recommendation,
and will correctly serialize XML 1.1 documents if the DOM level 3 load/save
APIs are in use.

%package        javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils

# Consolidating all javadocs into one package
Obsoletes:      %{name}-javadoc-impl < %{version}-%{release}
Obsoletes:      %{name}-javadoc-xs < %{version}-%{release}
Obsoletes:      %{name}-javadoc-xni < %{version}-%{release}
Obsoletes:      %{name}-javadoc-other < %{version}-%{release}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.

%package        demo
Summary:        Demonstrations and samples for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description    demo
%{summary}.

%prep
%setup -q -n xerces-%{cvs_version}
%patch0 -p0 -b .orig
%patch1 -p0 -b .orig

# Copy the custom ant tasks into place
mkdir -p tools/org/apache/xerces/util
mkdir -p tools/bin
cp -a %{SOURCE3} %{SOURCE5} %{SOURCE6} tools/org/apache/xerces/util

# Make sure upstream hasn't sneaked in any jars we don't know about
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

sed -i 's/\r//' LICENSE README NOTICE

%build
pushd tools

# Build custom ant tasks
javac -classpath $(build-classpath ant) org/apache/xerces/util/XJavac.java
jar cf bin/xjavac.jar org/apache/xerces/util/XJavac.class

# Build custom doc taglets
javac -classpath /usr/lib/jvm/java/lib/tools.jar org/apache/xerces/util/*Taglet.java
jar cf bin/xerces2taglets.jar org/apache/xerces/util/*Taglet.class

ln -sf $(build-classpath xalan-j2) serializer.jar
ln -sf $(build-classpath xml-commons-apis) xml-apis.jar
ln -sf $(build-classpath xml-commons-resolver) resolver.jar
popd

# Build everything
export ANT_OPTS="-Xmx256m -Djava.endorsed.dirs=$(pwd)/tools -Djava.awt.headless=true -Dbuild.sysclasspath=first -Ddisconnected=true"
ant -Djavac.source=1.5 -Djavac.target=1.5 \
    -Dbuild.compiler=modern \
    clean jars javadocs

%install
# jars
install -pD -T build/xercesImpl.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
mkdir -p %{buildroot}%{_javadocdir}/%{name}/impl
mkdir -p %{buildroot}%{_javadocdir}/%{name}/xs
mkdir -p %{buildroot}%{_javadocdir}/%{name}/xni
mkdir -p %{buildroot}%{_javadocdir}/%{name}/other

cp -pr build/docs/javadocs/xerces2/* %{buildroot}%{_javadocdir}/%{name}/impl
cp -pr build/docs/javadocs/api/* %{buildroot}%{_javadocdir}/%{name}/xs
cp -pr build/docs/javadocs/xni/* %{buildroot}%{_javadocdir}/%{name}/xni
cp -pr build/docs/javadocs/other/* %{buildroot}%{_javadocdir}/%{name}/other

# scripts
install -pD -m755 -T %{SOURCE1} %{buildroot}%{_bindir}/%{name}-version
install -pD -m755 -T %{SOURCE2} %{buildroot}%{_bindir}/%{name}-constants

# manual pages
install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE11} %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE12} %{buildroot}%{_mandir}/man1

# demo
install -pD -T build/xercesSamples.jar %{buildroot}%{_datadir}/%{name}/%{name}-samples.jar
cp -pr data %{buildroot}%{_datadir}/%{name}

# Pom
install -pD -T -m 644 %{SOURCE7} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Depmap with legacy depmaps for compatability
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "xerces:xerces" -a "xerces:xmlParserAPIs"

# jaxp_parser_impl ghost symlink
ln -s %{_sysconfdir}/alternatives \
  %{buildroot}%{_javadir}/jaxp_parser_impl.jar
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxp_parser_impl_xerces-j2<<EOF
%{_javadir}/jaxp_parser_impl.jar	%{_javadir}/%{name}.jar	40
EOF

%files
%_altdir/jaxp_parser_impl_xerces-j2
%doc LICENSE NOTICE README
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*
%{_javadir}/%{name}*
%{_bindir}/*
%{_mandir}/*/*

%files javadoc
%{_javadocdir}/%{name}/impl
%{_javadocdir}/%{name}/xs
%{_javadocdir}/%{name}/xni
%{_javadocdir}/%{name}/other

%files demo
%{_datadir}/%{name}

%changelog
* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.11.0-alt1_14jpp7
- new release

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.11.0-alt1_11jpp7
- fc update

* Sat Mar 30 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt4_2jpp6
- bugfixes

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_2jpp6
- added pom

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt2_2jpp6
- build w/java6

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt1_2jpp6
- added OSGi provides

* Tue Jan 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.9.0-alt6_12jpp5
- added repolib as in jpp 5.0 template

* Sat Apr 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.9.0-alt5_2jpp1.7
- fixed script permissions

* Wed Feb 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.9.0-alt4_2jpp1.7
- converted from JPackage by jppimport script

* Wed Feb 06 2008 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt4
- added Provides: xerces-j2-demo to demo.
- demo subpackage is now xerces-j2 compatible.

* Tue Aug 21 2007 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt3
- rebuilt with java-1.5.0

* Mon May 21 2007 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt2
- NMU: 
  * fixes for X-less build
  * fixed bug in alternatives (jaxp_parser_impl.jar)
  * javadocs are split almost as they should be
  * added scripts subpackage

* Tue Apr 24 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.9.0-alt1
- 2.9.0 

* Tue Apr 24 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.8.1-alt2
- fix build with java-1.6-sun
- add compatibility with JPackage

* Wed Nov 15 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Sat Mar 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.0-alt1
- 2.8.0
- Updated Patch1

* Sun Feb 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.1-alt2
- Fixes to build with JDK 1.5

* Wed Jul 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.1-alt1
- New upstream release

* Mon Jun 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt1
- New upstream release
- Raised jaxp_parser_impl.jar alternative level to 130
  to reflect the JAXP 1.3 implementation
- Updated Patch1
- Use rpm-build-java macros
- Conditionally build samples, disabled by default
  (can not compile with 1.4.2)

* Tue Aug 31 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt2
- New alternatives format

* Mon Mar 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt1
- Remove JDK version hardcoding

* Sun Feb 22 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt0.1
- Updated to upstream release 2.6.2

* Wed Jan 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt3.1
- Temporarily hardcode the JDK

* Sat Dec 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt3
- Patches from Alexey Borovskoy
- Use xvfb-run to start fake X server
- Migration to new alternatives scheme

* Sat Dec 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt2
- Added update-alternatives to install-time dependencies
- Corrected timing of updating alternatives during uninstall/upgrade
- Set JAVA_HOME to the commonly known J2SE directory

* Thu Dec 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt1
- New upstream release

* Thu Sep 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.0-alt1
- Updated to 2.5.0, renamed to xerces-j because xerces 1.x is obsolete
- Dropped README from the docs as it contains nothing but build instructions
- Remove JAXP api docs from javadoc, link to xml-commons-apis instead

* Sun Nov 17 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.1-alt1
- Ported the package over from the JPackage project. Thank you guys.
