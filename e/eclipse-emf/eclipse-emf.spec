# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name eclipse-emf
%define version 2.9.1
%{?scl:%scl_package eclipse-emf}
%{!?scl:%global pkg_name %{name}}


%if 0%{?rhel} >= 6
%global debug_package %{nil}
%endif
%global eclipse_dropin   %{_datadir}/eclipse/dropins

%global emf_tag R2_9_1
%global context_qualifier v20130930-0823

%define __requires_exclude osgi*

Name:      %{?scl_prefix}eclipse-emf
Version:   2.9.1
Release:   alt1_1jpp7 
Summary:   Eclipse Modeling Framework (EMF) Eclipse plugin
Group:     System/Libraries
License:   EPL
URL:       http://www.eclipse.org/modeling/emf/

# source tarball and the script used to generate it from upstream's source control
# script usage:
# $ sh get-emf.sh
Source0:   emf-%{emf_tag}.tar.gz
Source1:   get-emf.sh

# don't depend on ANT_HOME and JAVA_HOME environment vars, patch upstream
#Patch0:    %{name}-make-homeless.patch
# look inside correct directory for platform docs
Patch1:    %{pkg_name}-platform-docs-location.patch
# Build docs correctly
Patch3:    %{pkg_name}-build-docs.patch
# Remove xsd2ecore components from SDK, they are not in the main feature
Patch4:    %{pkg_name}-no-xsd2ecore.patch
Patch5:    %{pkg_name}-fix-missing-index.patch

BuildArch:        noarch

# we require 1.6.0 because the javadocs fail to build otherwise
BuildRequires:    java-javadoc
BuildRequires:    jpackage-utils
BuildRequires:    %{?scl_prefix}eclipse-pde >= 1:4.2.0
BuildRequires:    dos2unix
Requires:         jpackage-utils
Requires:         %{?scl_prefix}eclipse-platform >= 1:4.2.0
Requires:         %{name}-core

# the standalone package was deprecated and removed in EMF 2.3 (see eclipse.org bug #191837)
Obsoletes:        %{name}-standalone < 2.4

# the SDO sub-project was terminated upstream and removed in EMF 2.5 (see eclipse.org bug #251402)
Obsoletes:        %{name}-sdo < 2.5
Obsoletes:        %{name}-sdo-sdk < 2.5
Source44: import.info

#TODO: ODA, GWT and RAP components are not packaged.
#TODO: Possibly spin XSD off into it's own package, upstream have moved it to it's project

%description
The Eclipse Modeling Framework (EMF) allows developers to build tools and
other applications based on a structured data model. From a model
specification described in XMI, EMF provides tools and runtime support to
produce a set of Java classes for the model, along with a set of adapter
classes that enable viewing and command-based editing of the model, and a
basic editor.

%package   core
Epoch:      1
Summary:   Eclipse EMF Core
Group:     System/Libraries
Obsoletes: eclipse-emf-core < 1:2.8.0-20

%description core
The core of Eclipse Modeling Framework
 
%package   sdk
Summary:   Eclipse EMF SDK
Group:     System/Libraries
Requires:  java-javadoc
Requires:  %{?scl_prefix}eclipse-pde >= 1:4.2.0
Requires:  %{name} = %{version}-%{release}

%description sdk
Documentation and source for the Eclipse Modeling Framework (EMF).

%package   xsd
Summary:   XML Schema Definition (XSD) Eclipse plugin
Group:     System/Libraries
Requires:  %{name} = %{version}-%{release}

%description xsd
The XML Schema Definition (XSD) plugin is a library that provides an API for
manipulating the components of an XML Schema as described by the W3C XML
Schema specifications, as well as an API for manipulating the DOM-accessible
representation of XML Schema as a series of XML documents.

%package   xsd-sdk
Summary:   Eclipse XSD SDK
Group:     System/Libraries
Requires:  java-javadoc
Requires:  %{?scl_prefix}eclipse-pde >= 1:4.2.0
Requires:  %{name}-xsd = %{version}-%{release}
Requires:  %{name}-sdk = %{version}-%{release}

%description xsd-sdk
Documentation and source for the Eclipse XML Schema Definition (XSD) plugin.

%package   examples
Summary:   Eclipse EMF/XSD examples
Group:     System/Libraries
Requires:  %{name} = %{version}-%{release}
Requires:  %{name}-xsd = %{version}-%{release}

%description examples
Installable versions of the example projects from the SDKs that demonstrate how
to use the Eclipse Modeling Framework (EMF) and XML Schema Definition (XSD)
plugins.

%prep
%setup -q -n emf-%{version}
%patch1 -p0 -b .orig
#https://bugs.eclipse.org/bugs/show_bug.cgi?id=406981
#%patch2 -p1 -b .orig
%patch3 -p1 -b .orig
%patch4 -p1 -b .orig
%patch5

rm org.eclipse.emf.doc/tutorials/jet2/jetc-task.jar
rm org.eclipse.emf.test.core/data/data.jar

# link to local java api javadocs
sed -i -e "s|http://java.sun.com/j2se/1.5/docs/api/|%{_javadocdir}/java|" -e "s|\${javaHome}/docs/api/|%{_javadocdir}/java|" \
  org.eclipse.emf.doc/build/javadoc.xml.template \
  org.eclipse.xsd.doc/build/javadoc.xml.template

# make sure upstream hasn't sneaked in any jars we don't know about
JARS=""
for j in `find -name "*.jar"`; do
  if [ ! -L $j ]; then
    JARS="$JARS $j"
  fi
done
if [ ! -z "$JARS" ]; then
   echo "These jars should be deleted and symlinked to system jars: $JARS"
   exit 1
fi

%build
# Note: We use forceContextQualifier because the docs plugins use custom build
#       scripts and don't work otherwise.
OPTIONS="-DjavacTarget=1.5 -DjavacSource=1.5 -DforceContextQualifier=%{context_qualifier}"

# Work around pdebuild entering/leaving symlink it is unaware of.
ln -s %{_builddir}/emf-%{version}/org.eclipse.emf.license-feature %{_builddir}/emf-%{version}/org.eclipse.emf.license
ln -s %{_builddir}/emf-%{version}/org.eclipse.xsd.license-feature %{_builddir}/emf-%{version}/org.eclipse.xsd.license

# We build the emf, xsd and examples features seperately, rather than just
# building the "all" feature, because it makes the files section easier to
# maintain (i.e. we don't have to know when upstream adds a new plugin)

# build core features
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.common -a "$OPTIONS"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.ecore -a "$OPTIONS"

# build emf features - order is important
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.edit -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.common.ui -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.edit.ui -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.ecore.edit -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.ecore.editor -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.codegen -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.codegen.ecore -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.mapping -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.mapping.ecore -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.codegen.ui -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.codegen.ecore.ui -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.mapping.ui -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.mapping.ecore.editor -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.databinding -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.databinding.edit -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.converter -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.sdk -a "$OPTIONS" -d "eclipse-emf-core"

# build xsd features
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.edit -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.editor -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.mapping -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.mapping.editor -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.ecore.converter -a "$OPTIONS" -d "eclipse-emf-core"
%{_bindir}/eclipse-pdebuild -f org.eclipse.xsd.sdk -a "$OPTIONS" -d "eclipse-emf-core"

# build examples features
%{_bindir}/eclipse-pdebuild -f org.eclipse.emf.examples -a "$OPTIONS" -d "eclipse-emf-core"

%install
install -d -m 755 %{buildroot}%{eclipse_dropin}
install -d -m 755 %{buildroot}%{_javadir}/emf

unzip -q -n -d %{buildroot}%{_javadir}/emf          build/rpmBuild/org.eclipse.emf.common.zip
unzip -q -n -d %{buildroot}%{_javadir}/emf          build/rpmBuild/org.eclipse.emf.ecore.zip
unzip -q -n -d %{buildroot}%{_javadir}/emf          build/rpmBuild/org.eclipse.emf.edit.zip


unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.common.ui.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.edit.ui.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.ecore.edit.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.ecore.editor.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.codegen.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.codegen.ecore.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.converter.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.codegen.ui.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.codegen.ecore.ui.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.mapping.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.mapping.ui.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.mapping.ecore.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.mapping.ecore.editor.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.databinding.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf          build/rpmBuild/org.eclipse.emf.databinding.edit.zip

unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf-sdk      build/rpmBuild/org.eclipse.emf.sdk.zip

unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.edit.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.editor.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.mapping.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.mapping.editor.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd          build/rpmBuild/org.eclipse.xsd.ecore.converter.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/xsd-sdk      build/rpmBuild/org.eclipse.xsd.sdk.zip
unzip -q -n -d %{buildroot}%{eclipse_dropin}/emf-examples build/rpmBuild/org.eclipse.emf.examples.zip

# the non-sdk builds are a subset of the sdk builds, so delete duplicate features & plugins from the sdks
(cd %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/features && ls %{buildroot}%{eclipse_dropin}/emf/eclipse/features | xargs rm -rf)
(cd %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins  && ls %{buildroot}%{eclipse_dropin}/emf/eclipse/plugins  | xargs rm -rf)
(cd %{buildroot}%{eclipse_dropin}/xsd-sdk/eclipse/features && ls %{buildroot}%{eclipse_dropin}/xsd/eclipse/features | xargs rm -rf)
(cd %{buildroot}%{eclipse_dropin}/xsd-sdk/eclipse/plugins  && ls %{buildroot}%{eclipse_dropin}/xsd/eclipse/plugins  | xargs rm -rf)

# remove duplicated plugins and features
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/features/org.eclipse.emf.common_*
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins/org.eclipse.emf.common_*
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/features/org.eclipse.emf.ecore_*
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins/org.eclipse.emf.ecore_*
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins/org.eclipse.emf.ecore.change_*
rm -rf %{buildroot}%{eclipse_dropin}/emf-sdk/eclipse/plugins/org.eclipse.emf.ecore.xmi_*

pushd %{buildroot}%{_javadir}/emf/eclipse/plugins/
for f in org.eclipse.emf.common \
		org.eclipse.emf.ecore.change \
		org.eclipse.emf.ecore.xmi \
		org.eclipse.emf.ecore \
		org.eclipse.emf.edit ; do
	mv ${f}_* ${f}.jar
done
popd
pushd %{buildroot}%{eclipse_dropin}/emf/eclipse/plugins
	ln -s %{_javadir}/emf/eclipse/plugins/org.eclipse.emf.edit.jar
popd
%files
%{eclipse_dropin}/emf
%doc org.eclipse.emf.license-feature/rootfiles/*

%files core
%{_javadir}/emf
%doc org.eclipse.emf.license-feature/rootfiles/*

%files sdk
%{eclipse_dropin}/emf-sdk

%files xsd
%{eclipse_dropin}/xsd
%doc org.eclipse.xsd.license-feature/rootfiles/*

%files xsd-sdk
%{eclipse_dropin}/xsd-sdk

%files examples
%{eclipse_dropin}/emf-examples

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_1jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt1_0.1.git352e28jpp7
- new version

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_7jpp7
- fc update

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt2_16jpp7
- applied repocop patches

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt1_16jpp7
- new version

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_1jpp6
- new version

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 2.7.0-alt1_1jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1_2jpp6
- new version

* Tue Jan 26 2010 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_4jpp6
- new version

