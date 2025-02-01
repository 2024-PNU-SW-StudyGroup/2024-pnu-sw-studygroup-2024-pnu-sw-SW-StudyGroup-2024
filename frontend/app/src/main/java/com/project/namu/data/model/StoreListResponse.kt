package com.project.namu.data.model

import com.google.gson.annotations.SerializedName

data class StoreData(
    @SerializedName("storeId") val storeId: Int,
    @SerializedName("storeName") val storeName: String,
    @SerializedName("storeCategory") val storeCategory: String,
    @SerializedName("pickupTimes") val pickupTimes: String,
    @SerializedName("minPrice") val minPrice: Int,
    @SerializedName("reviewCount") val reviewCount: Int,
    @SerializedName("orderCount") val orderCount: Int,
    @SerializedName("storeRating") val storeRating: Float,
    @SerializedName("location") val location: Int,

    @SerializedName("open") val open: Boolean,
    @SerializedName("setNames") val setNames: List<SetInfo>
)

data class SetInfo(
    @SerializedName("setName") val setName: String,
    @SerializedName("menuNames") val menuNames: String = ""
)
data class StoreDetailData(
    @SerializedName("storeId") val storeId: Int,
    @SerializedName("storeName") val storeName: String,
    @SerializedName("storeCategory") val storeCategory: String,
    @SerializedName("pickupTimes") val pickupTimes: String,
    @SerializedName("minPrice") val minPrice: Int,
    @SerializedName("reviewCount") val reviewCount: Int,
    @SerializedName("orderCount") val orderCount: Int,
    @SerializedName("storeRating") val storeRating: Int,
    @SerializedName("location") val location: Int,
    @SerializedName("setNames") val setNames: List<SetInfo>,
    @SerializedName("open") val open: Boolean,
    @SerializedName("storePictureUrl") val storePictureUrl: String? = null,
    @SerializedName("storePhone") val storePhone: String? = null,
    @SerializedName("storeAddress") val storeAddress: String? = null,

    )

data class DetailMenu(
    @SerializedName("set_name") val setName: String,
    @SerializedName("menu_names") val menuNames: String,
    @SerializedName("menu_price") val menuPrice: Int,
    @SerializedName("menu_discount_price") val menuDiscountPrice: Int,
    @SerializedName("menu_picture_url") val menuPictureUrl: String,
    @SerializedName("popularity") val popularity: Boolean,
    @SerializedName("menu_detail") val menuDetail: String
)
