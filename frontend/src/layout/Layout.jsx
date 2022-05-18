import React from "react";
import { Outlet } from "react-router-dom";
import styles from "./Layout.module.css";
import Footer from "../components/Footer/Footer";
import Navbar from "../components/Navbar/Navbar";

const Layout = () => {
  return (
    <>
      <Navbar />
      <main className={styles.container}>
        <Outlet />
      </main>
      <Footer />
    </>
  );
};

export default Layout;
