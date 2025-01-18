package com.project.namu.ui.component

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import com.project.namu.ui.page.HomeScreen
import com.project.namu.ui.page.LoginScreen
import com.project.namu.ui.page.MypageScreen
import com.project.namu.ui.page.Search_listScreen

@Composable
fun NavGraph(navController: NavHostController) {
    NavHost(navController = navController, startDestination = "검색") {
        composable("로그인") { LoginScreen(navController) }
        composable("회원가입") { MypageScreen(navController) }
        composable("홈") { HomeScreen(navController) }
        composable("검색") { Search_listScreen(navController) }  // 검색 화면 추가
    }
}