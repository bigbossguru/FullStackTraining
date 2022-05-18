import React from "react";
import styles from "./Navbar.module.css";
import { Link } from "react-router-dom";

const NavbarSimple = () => {
  return (
    <header>
      <Link to="/" className={styles.logo}>
        <h2>FullStackTrainig</h2>
      </Link>
    </header>
  );
};

export default NavbarSimple;
