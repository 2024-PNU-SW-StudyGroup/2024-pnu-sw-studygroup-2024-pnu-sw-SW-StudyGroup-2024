package com.project.namu.data.repository

import com.project.namu.data.model.StoreData
import com.project.namu.data.remote.ApiService
import retrofit2.Response

class StoreRepository(private val apiService: ApiService) {
    suspend fun getStoreList(): Response<List<StoreData>> {
        return apiService.getStoreList()
    }
}