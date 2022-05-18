import React from "react";
import styles from "./Footer.module.css";

const Footer = () => {
  return (
    <footer>
      <div className={styles.footer_content}>
        <h3>FullStack Trainig</h3>
        <p>
          FullStack Trainig is huge project and open sourse for allow us
          training new different skill and play
        </p>
      </div>
      <div className={styles.footer_bottom}></div>
    </footer>
  );
};

export default Footer;
