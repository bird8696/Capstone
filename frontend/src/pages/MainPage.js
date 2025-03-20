import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import mainImage from "../images/MainPage.png";
import { motion } from "framer-motion";

const MainPage = () => {
  const navigate = useNavigate();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // 컴포넌트가 처음 렌더링될 때 로그인 상태 확인
  useEffect(() => {
    const loggedInStatus = localStorage.getItem("isLoggedIn") === "true";
    setIsLoggedIn(loggedInStatus);
  }, []);

  // 로그인 함수
  const handleLogin = () => {
    localStorage.setItem("isLoggedIn", "true");
    setIsLoggedIn(true);
  };

  // 로그아웃 함수
  const handleLogout = () => {
    localStorage.removeItem("isLoggedIn");
    setIsLoggedIn(false);
  };

  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      height: "100vh",
      backgroundColor: "#f5f5f5",
      overflow: "hidden"
    }}>
      <motion.h1 
        style={{ marginBottom: "30px", fontSize: "40px" }}
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
      >
        AI MOCK INTERVIEW SYSTEM
      </motion.h1>
      
      {/* 버튼 애니메이션 */}
      {[
        { text: "Sign up", action: () => navigate("/register") },
        { text: isLoggedIn ? "Sign out" : "Sign in", action: isLoggedIn ? handleLogout : () => { handleLogin(); navigate("/login"); } },
        { text: "Interview begins", action: () => navigate("/interview"), disabled: !isLoggedIn }
      ].map((button, index) => (
        <motion.button 
          key={button.text}
          style={{
            width: "240px", padding: "15px", marginBottom: "10px", fontSize: "16px",
            backgroundColor: button.disabled ? "#ccc" : "#D99E00", color: "white", 
            border: "none", cursor: button.disabled ? "not-allowed" : "pointer",
            borderRadius: "5px"
          }} 
          onClick={button.action}
          disabled={button.disabled}
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut", delay: index * 0.2 }}
        >
          {button.text}
        </motion.button>
      ))}
      
      {/* 이미지 애니메이션 추가 */}
      <motion.img 
        src={mainImage} 
        alt="Main" 
        style={{ width: "50%", maxWidth: "600px", borderRadius: "10px" }}
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut", delay: 0.6 }}
      />
    </div>
  );
};

export default MainPage;
