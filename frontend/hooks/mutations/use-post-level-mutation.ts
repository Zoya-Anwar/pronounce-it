import { apiClient } from "@/lib/interceptor";
import { useMutation, useQueryClient, UseMutationOptions } from "react-query";
import z from "zod";

// type of the data that will be passed to the mutation is string for level difficulty

const requestSchema = z.object({
  level: z.string(),
});

type RequestData = z.infer<typeof requestSchema>;

const postLevel = async (data: RequestData) => {
  const response = await apiClient.post("/level", data);
  return response;
};

type UsePostLevelMutationOptions = Omit<
  UseMutationOptions<unknown, unknown, RequestData, unknown>,
  "mutationFn"
>;

export const usePostLevelMutation = (options?: UsePostLevelMutationOptions) => {
  const queryClient = useQueryClient();
  return useMutation(postLevel, {
    onSuccess: () => {},
    ...options,
  });
};
