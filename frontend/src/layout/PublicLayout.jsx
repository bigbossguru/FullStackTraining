import React from "react";
import { Outlet } from "react-router-dom";
import Footer from "../components/Footer/Footer";
import NavbarSimple from "../components/Navbar/NavbarSimple";

const PublicLayout = () => {
  return (
    <>
      <NavbarSimple />
      <Outlet />
      <Footer />
    </>
  );
};

export default PublicLayout;
