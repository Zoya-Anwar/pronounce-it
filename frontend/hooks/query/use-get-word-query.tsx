import { apiClient } from "@/lib/interceptor";
import { useQuery, useQueryClient, UseQueryOptions } from "react-query";
import z from "zod";

const responseSchema = z.object({
    word: z.string(),
  });
  
  export type ResponseData = z.infer<typeof responseSchema>;
  
  const getWord = async () => {
    const {
      data
    } = await apiClient.get<ResponseData>("/get_word");
    return data;
  };
  
  type UseGetWordQueryOptions = Omit<
    UseQueryOptions<unknown, unknown, ResponseData>,
    "queryFn"
  >;
  
  export const useGetWordQuery = (options?: UseGetWordQueryOptions) => {
    const queryClient = useQueryClient();
    return useQuery({
      queryFn: getWord,
      onSuccess: (data: ResponseData) => {},
      ...options,
    });
  };