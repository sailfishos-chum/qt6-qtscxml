%global  qt_version 6.7.2

Summary: Qt6 - ScXml component
Name:    qt6-qtscxml
Version: 6.7.2
Release: 0%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
Source0: %{name}-%{version}.tar.bz2


BuildRequires: cmake
BuildRequires: clang
BuildRequires: ninja
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{qt_version}
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: openssl-devel

%description
The Qt SCXML module provides functionality to create state machines from SCXML files.
This includes both dynamically creating state machines loading the SCXML file and instantiating states and transitions)
and generating a C++ file that has a class implementing the state machine.
It also contains functionality to support data models and executable content.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=OFF \
  -DQT_INSTALL_EXAMPLES_SOURCES=OFF

%cmake_build

%install
%cmake_install


%files
%license LICENSES/*
%{_qt6_libdir}/libQt6Scxml.so.6*
%{_qt6_libdir}/libQt6ScxmlQml.so.6*
%{_qt6_libdir}/libQt6StateMachineQml.so.6*
%{_qt6_libdir}/libQt6StateMachine.so.6*
%{_qt6_libexecdir}/qscxmlc
%{_qt6_qmldir}/QtScxml/
%{_qt6_qmldir}/QtQml/
%{_qt6_plugindir}/scxmldatamodel/libqscxmlecmascriptdatamodel.so

%files devel
%{_qt6_headerdir}/QtScxml/
%{_qt6_headerdir}/QtScxmlQml/
%{_qt6_headerdir}/QtStateMachineQml
%{_qt6_headerdir}/QtStateMachine/
%{_qt6_libdir}/libQt6Scxml.so
%{_qt6_libdir}/libQt6Scxml.prl
%{_qt6_libdir}/libQt6ScxmlQml.prl
%{_qt6_libdir}/libQt6ScxmlQml.so
%{_qt6_libdir}/libQt6StateMachine.prl
%{_qt6_libdir}/libQt6StateMachine.so
%{_qt6_libdir}/libQt6StateMachineQml.prl
%{_qt6_libdir}/libQt6StateMachineQml.so
%{_qt6_libdir}/cmake/Qt6Scxml
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtScxmlTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6ScxmlQml/*.cmake
%{_qt6_libdir}/cmake/Qt6ScxmlTools/*.cmake
%{_qt6_libdir}/cmake/Qt6StateMachine/*.cmake
%{_qt6_libdir}/cmake/Qt6StateMachineQml/*.cmake
%{_qt6_archdatadir}/mkspecs/features/qscxmlc.prf
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/*.pc
